from locust import HttpUser, TaskSet, task, between
from core.locust.common import get_csrf_token
from core.environment.host import get_host_for_locust_testing


class StagingArea(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
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
                    if response.status_code == 200:
                        response.success()
                    else:
                        response.failure("Login failed")
            else:
                response.failure("Failed to get CSRF token")
    
    @task(1)
    def get_staging_area(self):
        with self.client.get("/dataset/list", name="Get Staging Area", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to get dataset")
    
    @task(2)
    def stage_all_datasets(self):
        with self.client.post("/dataset/stage/all", name="Stage All Datasets", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to stage all datasets")

    @task(3)
    def unstage_all_datasets(self):
        with self.client.post("/dataset/unstage/all", name="Unstage All Datasets", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to unstage all datasets")
    
    @task(4)
    def stage_dataset(self):
        with self.client.post("/dataset/stage/255", name="Stage Dataset", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to stage dataset")

    @task(5)
    def unstage_dataset(self):
        with self.client.post("/dataset/unstage/255", name="Stage Dataset", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to unstage dataset")
    
    @task(6)
    def publish_dataset(self):
        with self.client.post("/dataset/publish", name="Publish Dataset", catch_response=True) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to publish dataset")


    
class StagingAreaActions(HttpUser):
    tasks = [StagingArea]
    wait_time = between(5, 9)
    host = get_host_for_locust_testing()
