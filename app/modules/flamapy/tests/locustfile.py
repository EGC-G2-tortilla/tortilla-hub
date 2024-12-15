from locust import HttpUser, TaskSet, task
from core.environment.host import get_host_for_locust_testing
from io import BytesIO


class FlamapyBehavior(TaskSet):
    def on_start(self):
        self.validate_valid_uvl()

    @task
    def validate_valid_uvl(self):
        """
        Envía un UVL válido al endpoint y verifica la respuesta.
        """
        valid_uvl_content = """features
    Chat
        mandatory
            Connection
                alternative
                    "Peer 2 Peer"
                    Server
            Messages
                or
                    Text
                    Video
                    Audio
        optional
            "Data Storage"
            "Media Player"

constraints
    Server => "Data Storage"
    Video | Audio => "Media Player"
"""
        files = {
            "file": ("valid_model.uvl", BytesIO(valid_uvl_content.encode("utf-8")))
        }
        response = self.client.post("/flamapy/validate_uvl", files=files)

        if response.status_code != 200:
            print(f"Validation of valid UVL failed: {response.status_code}")

    @task
    def validate_empty_uvl(self):
        """
        Envía un UVL vacío al endpoint y verifica la respuesta.
        """
        empty_uvl_content = ""

        # Simular la subida de un archivo vacío
        files = {
            "file": ("empty_model.uvl", BytesIO(empty_uvl_content.encode("utf-8")))
        }

        # Hacer la petición POST al endpoint
        response = self.client.post("/flamapy/validate_uvl", files=files)

        # Verificar el estado HTTP de la respuesta
        if response.status_code != 400:
            print(f"❌ Expected 400 for empty UVL, got: {response.status_code}")
        else:
            try:
                # Procesar el cuerpo de la respuesta como JSON
                json_data = response.json()
                if "errors" not in json_data or len(json_data["errors"]) == 0:
                    print(
                        "❌ Validation failed, but no error details provided in response."
                    )
                elif (
                    json_data["errors"][0]
                    != "The UVL file is empty and cannot be processed."
                ):
                    print(f"❌ Unexpected error message: {json_data['errors'][0]}")
                else:
                    print("✅ Validation of empty UVL returned expected error.")
            except ValueError:
                print(f"❌ Invalid JSON in response: {response.text}")

    @task
    def validate_invalid_uvl(self):
        invalid_uvl_content = """
        features
            Root

        constraints:
        """
        files = {
            "file": ("invalid_model.uvl", BytesIO(invalid_uvl_content.encode("utf-8")))
        }
        response = self.client.post("/flamapy/validate_uvl", files=files)

        # Verificar que el estado es 400
        if response.status_code != 400:
            print(f"Unexpected status code: {response.status_code}")
        else:
            json_data = response.json()
            if "errors" not in json_data or len(json_data["errors"]) == 0:
                print("Expected errors in response, but none were provided.")
            else:
                print("Validation of invalid UVL returned expected errors.")


class FlamapyUser(HttpUser):
    tasks = [FlamapyBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
