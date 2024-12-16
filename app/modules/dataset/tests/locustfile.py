from locust import HttpUser, TaskSet, between, task
from core.locust.common import get_csrf_token
from core.environment.host import get_host_for_locust_testing


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
    tasks = [DashboardBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()


class ViewDatasetBehavior(TaskSet):

    def on_start(self):
        """Simula el inicio de sesión antes de cualquier tarea."""
        self.login()

    @task(1)
    def view_dataset(self):
        """Simula la visualización de un dataset."""
        dataset_doi = "10.1234/dataset1"
        with self.client.get(
            f"/dataset/{dataset_doi}", name="View Dataset", catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to view dataset")

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


class DownloadDatasetBehavior(TaskSet):

    def on_start(self):
        """Simula el inicio de sesión antes de cualquier tarea."""
        self.login()

    @task(1)
    def download_dataset(self):
        """Simula la descarga de un dataset."""
        dataset_id = 1
        with self.client.get(
            f"/dataset/download/{dataset_id}",
            name="Download Dataset",
            catch_response=True,
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to download dataset")

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


class ViewDatasetUser(HttpUser):
    """Simula usuarios que visualizan datasets."""

    tasks = [ViewDatasetBehavior]
    wait_time = between(5, 9)
    host = get_host_for_locust_testing()


class DownloadDatasetUser(HttpUser):
    """Simula usuarios que descargan datasets."""

    tasks = [DownloadDatasetBehavior]
    wait_time = between(5, 9)
    host = get_host_for_locust_testing()
