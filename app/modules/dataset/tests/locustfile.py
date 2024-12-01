from locust import HttpUser, TaskSet, task
from core.locust.common import get_csrf_token
from core.environment.host import get_host_for_locust_testing


class DatasetBehavior(TaskSet):
    def on_start(self):
        self.dataset()

    @task
    def dataset(self):
        response = self.client.get("/dataset/upload")
        get_csrf_token(response)


class DashboardBehavior(TaskSet):

    @task(2)
    def view_dashboard(self):
        """Simula la carga del dashboard principal."""
        with self.client.get(
            "/", name="View Dashboard", catch_response=True
        ) as response:
            if response.status_code == 200 and "Welcome to UVLHub.io!" in response.text:
                response.success()
            else:
                response.failure("Failed to load dashboard")

    @task(1)
    def download_dataset(self):
        """Simula la descarga de un dataset."""
        with self.client.get(
            "/dataset/download/1", name="Download Dataset", catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to download dataset")

    @task(1)
    def explore_datasets(self):
        """Simula la navegación a la sección de exploración de datasets."""
        with self.client.get(
            "/explore", name="Explore Datasets", catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to explore datasets")


class DatasetUser(HttpUser):
    tasks = [DatasetBehavior, DashboardBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
