from locust import HttpUser, TaskSet, task, between
from core.locust.common import get_csrf_token
from core.environment.host import get_host_for_locust_testing
                
class DownloadAllAuthBehavior(TaskSet):
    def on_start(self):
        """Simula el inicio de sesión antes de cualquier tarea."""
        self.login()
        
    @task(1)
    def download_all_authenticated(self):
        "Simula la descarga de todos los datasets estando logueado."
        with self.client.get("/dataset/download_all", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to download all datasets")
    
    def login(self):
        """Simula el inicio de sesión."""
        with self.client.get(
            "/login", name="Login Page", catch_response=True
        ) as response:
            csrf_token = get_csrf_token(response)
            if csrf_token:
                login_data = {
                    "username": "user1@example.com",
                    "password": "1234",
                    "csrf_token": csrf_token,
                }
                with self.client.post(
                    "/login", data=login_data, name="Login", catch_response=True
                ) as response:
                    if response.status_code == 200 and "Welcome" in response.text:
                        response.success()
                    else:
                        response.failure("Login failed")
            else:
                response.failure("Failed to get CSRF token")
    
class DownloadAllAuthUser(HttpUser):
    tasks = [DownloadAllAuthBehavior]
    wait_time = between(5, 9)
    host = get_host_for_locust_testing()