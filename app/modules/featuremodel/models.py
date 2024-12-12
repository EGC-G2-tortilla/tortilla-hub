from app import db
from sqlalchemy import Enum as SQLAlchemyEnum

from app.modules.dataset.models import Author, PublicationType


class FeatureModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data_set_id = db.Column(db.Integer, db.ForeignKey("data_set.id"), nullable=False)
    fm_meta_data_id = db.Column(db.Integer, db.ForeignKey("fm_meta_data.id"))
    files = db.relationship(
        "Hubfile", backref="feature_model", lazy=True, cascade="all, delete"
    )
    fm_meta_data = db.relationship(
        "FMMetaData", uselist=False, backref="feature_model", cascade="all, delete"
    )

    def __repr__(self):
        return f"FeatureModel<{self.id}>"

    def get_fact_labels(self):
        metrics = self.fm_meta_data.fm_metrics if self.fm_meta_data and self.fm_meta_data.fm_metrics else None
        return {
            "id": self.id,
            "title": self.fm_meta_data.title if self.fm_meta_data else None,
            "uvl_filename": self.fm_meta_data.uvl_filename if self.fm_meta_data else None,
            "metrics": metrics.to_dict() if metrics else None,
        }

    @staticmethod
    def extract_features(uvl_file_path):
        parser = UVLParser()
        model_data = parser.parse(uvl_file_path)
        return model_data["features"]

    @staticmethod
    def extract_constraints(uvl_file_path):
        parser = UVLParser()
        model_data = parser.parse(uvl_file_path)
        return model_data["constraints"]

    @staticmethod
    def calculate_max_depth(features):
        parser = UVLParser()
        model_data = parser.parse(features)
        return model_data["max_depth"]

    @staticmethod
    def calculate_variability(features, constraints):
        """
        Calcula la variabilidad del modelo.
        """
        if not features:
            return 0.0
        # Ejemplo: consideramos que cada restricción reduce la variabilidad
        return len(constraints) / len(features) if features else 0.0

    def calculate_metrics(self, file_path):
        parser = UVLParser()
        model_data = parser.parse(file_path)

        # Asignar métricas a los campos correspondientes
        self.fm_meta_data.fm_metrics = self.fm_meta_data.fm_metrics or FMMetrics()
        self.fm_meta_data.fm_metrics.number_of_features = len(model_data["features"])
        self.fm_meta_data.fm_metrics.constraints_count = len(model_data["constraints"])
        self.fm_meta_data.fm_metrics.max_depth = model_data["max_depth"]
        self.fm_meta_data.fm_metrics.variability = self.calculate_variability(
            model_data["features"], model_data["constraints"]
        )

    def to_dict(self):
        return {
            "id": self.id,
            "fact_labels": self.get_fact_labels(),  # Añadido
            "files": [file.to_dict() for file in self.files],
        }


class FMMetaData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uvl_filename = db.Column(db.String(120), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=False)
    publication_type = db.Column(SQLAlchemyEnum(PublicationType), nullable=False)
    publication_doi = db.Column(db.String(120))
    tags = db.Column(db.String(120))
    uvl_version = db.Column(db.String(120))
    fm_metrics_id = db.Column(db.Integer, db.ForeignKey("fm_metrics.id"))
    fm_metrics = db.relationship("FMMetrics", uselist=False, backref="fm_meta_data")
    authors = db.relationship(
        "Author",
        backref="fm_metadata",
        lazy=True,
        cascade="all, delete",
        foreign_keys=[Author.fm_meta_data_id],
    )

    def __repr__(self):
        return f"FMMetaData<{self.title}"

    def to_dict(self):
        return {
            "id": self.id,
            "uvl_filename": self.uvl_filename,
            "title": self.title,
            "description": self.description,
            "publication_type": self.publication_type.value,
            "publication_doi": self.publication_doi,
            "tags": self.tags.split(",") if self.tags else [],
            "uvl_version": self.uvl_version,
            "metrics": self.fm_metrics.to_dict() if self.fm_metrics else None,  # Añadido
            "authors": [author.to_dict() for author in self.authors],
        }


class FMMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solver = db.Column(db.Text)  # Información sobre el solver
    not_solver = db.Column(db.Text)  # Información sobre restricciones no resueltas
    number_of_features = db.Column(db.Integer)  # Número de características en el modelo
    constraints_count = db.Column(db.Integer)  # Número de restricciones en el modelo
    max_depth = db.Column(db.Integer)  # Profundidad máxima del árbol del modelo
    variability = db.Column(db.Float)  # Porcentaje de variabilidad (si aplica)

    def __repr__(self):
        return (
            f"FMMetrics<solver={self.solver}, not_solver={self.not_solver}, "
            f"features={self.number_of_features}, constraints={self.constraints_count}, "
            f"max_depth={self.max_depth}, variability={self.variability}>"
        )

    def to_dict(self):
        return {
            "solver": self.solver,
            "not_solver": self.not_solver,
            "number_of_features": self.number_of_features,
            "constraints_count": self.constraints_count,
            "max_depth": self.max_depth,
            "variability": self.variability,
        }


class UVLParser:
    def parse(self, file_path):
        features = []
        constraints = []
        max_depth = 0

        with open(file_path, 'r') as file:
            lines = file.readlines()

        current_depth = 0
        for line in lines:
            line = line.strip()

            # Procesar características
            if line.startswith("features"):
                current_depth = 0
            elif line and not line.startswith("constraints"):
                if (
                    line.startswith("mandatory")
                    or line.startswith("optional")
                    or line.startswith("alternative")
                    or line.startswith("or")
                ):
                    current_depth += 1
                elif line.endswith(";"):
                    feature_name = line.strip(";").strip('"')
                    features.append(feature_name)
                    max_depth = max(max_depth, current_depth)

            # Procesar restricciones
            elif line.startswith("constraints"):
                continue
            elif line:
                constraints.append(line)

        return {
            "features": features,
            "constraints": constraints,
            "max_depth": max_depth,
        }
