import os
from venv import logger
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

    @property
    def fact_labels(self):
        """
        Calcula y devuelve los fact labels para este FeatureModel.
        """
        try:
            if not self.files:
                return {
                    "number_of_features": 0,
                    "constraints_count": 0,
                    "max_depth": 0,
                    "variability": 0.0,
                }
            # Obtener el primer archivo asociado y calcular sus métricas
            return self.files[0].get_fact_labels()
        except Exception as e:
            logger.error(
                f"Error calculating fact labels for FeatureModel {self.id}: {str(e)}"
            )
            return {
                "number_of_features": 0,
                "constraints_count": 0,
                "max_depth": 0,
                "variability": 0.0,
            }

    def get_fact_labels(self):
        """
        Calcula métricas para el modelo de características.
        """
        try:
            return self.files[0].get_fact_labels() if self.files else {}
        except Exception as e:
            raise RuntimeError(
                f"Error calculating fact labels for FeatureModel {self.id}: {str(e)}"
            )

    def __repr__(self):
        return f"FeatureModel<{self.id}>"


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


class FMMetrics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    solver = db.Column(db.Text)
    not_solver = db.Column(db.Text)

    def __repr__(self):
        return f"FMMetrics<solver={self.solver}, not_solver={self.not_solver}>"


class UVLParser:
    def parse(self, file_path):
        try:
            if not os.path.exists(file_path):
                # Manejar el caso en que el archivo no exista
                return {
                    "features": [],
                    "constraints": [],
                    "max_depth": 0,
                    "variability": 0.0,
                }

            features = []
            constraints = []

            # Leer el archivo UVL
            with open(file_path, "r") as file:
                lines = file.readlines()

            if not lines:
                raise ValueError("El archivo UVL está vacío.")

            in_features_section = False
            in_constraints_section = False

            for line in lines:
                line = line.strip()

                # Detectar secciones de características y restricciones
                if line.lower().startswith("features"):
                    in_features_section = True
                    in_constraints_section = False
                    continue
                elif line.lower().startswith("constraints"):
                    in_constraints_section = True
                    in_features_section = False
                    continue

                # Procesar características
                if in_features_section and line:
                    # Eliminar caracteres no deseados como ";" y comillas
                    feature_name = line.strip(";").strip('"')
                    if feature_name and not feature_name.startswith(
                        ("mandatory", "optional", "alternative", "or")
                    ):
                        features.append(feature_name)

                # Procesar restricciones
                elif in_constraints_section and line:
                    constraints.append(line)

            # Calcular la profundidad máxima utilizando una función auxiliar
            max_depth = self.calculate_max_depth(lines)

            if not features:
                raise ValueError("No se encontraron características en el archivo UVL.")

            return {
                "features": features,
                "constraints": constraints,
                "max_depth": max_depth,  # Calculado por la función auxiliar
                "variability": len(constraints) / len(features) if features else 0.0,
            }
        except FileNotFoundError:
            # Devolver valores predeterminados si el archivo no existe
            return {
                "features": [],
                "constraints": [],
                "max_depth": 0,
                "variability": 0.0,
            }
        except Exception as e:
            raise RuntimeError(f"Error al procesar el archivo UVL: {e}")

    # Función Auxiliar para Calcular la Max Depth
    def calculate_max_depth(self, lines):
        depth_stack = []  # Pila para rastrear profundidad
        max_depth = 0  # Profundidad máxima
        in_features_section = False
        found_features_section = False  # Bandera para detectar "features"

        for line in lines:
            stripped_line = line.strip()

            # Detectar inicio de la sección de características
            if stripped_line.lower().startswith("features"):
                in_features_section = True
                found_features_section = True  # Marcar que se encontró la sección
                depth_stack = []  # Reiniciar pila de profundidad
                continue
            elif stripped_line.lower().startswith("constraints"):
                in_features_section = False
                continue

            # Procesar solo líneas en la sección de características
            if in_features_section and stripped_line:
                leading_spaces = len(line) - len(line.lstrip())
                depth = (
                    leading_spaces // 4
                )  # Suponemos que 4 espacios equivalen a un nivel

                # Manejar la pila de profundidad
                while len(depth_stack) > depth:
                    depth_stack.pop()
                depth_stack.append(stripped_line)

                # Actualizar profundidad máxima
                max_depth = max(
                    max_depth, len(depth_stack) - 1
                )  # Restar 1 para excluir la raíz

        # Si no se encontró la sección "features", devolver profundidad 0
        if not found_features_section:
            return 0

        return max_depth
