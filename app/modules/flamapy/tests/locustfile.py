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
        files = {"file": ("valid_model.uvl", BytesIO(valid_uvl_content.encode("utf-8")))}
        response = self.client.post("/flamapy/validate_uvl", files=files)

        if response.status_code != 200:
            print(f"Validation of valid UVL failed: {response.status_code}")

 
class FlamapyUser(HttpUser):
    tasks = [FlamapyBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
