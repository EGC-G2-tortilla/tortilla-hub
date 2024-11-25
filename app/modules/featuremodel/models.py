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
        return {
            "id": self.id,
            "title": self.fm_meta_data.title,
            "uvl_filename": self.fm_meta_data.uvl_filename,
            "metrics": self.fm_meta_data.fm_metrics.to_dict() if self.fm_meta_data.fm_metrics else None,
        }

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

