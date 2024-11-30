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
    
    @task
    def dataset_stage(self):
        response = self.client.post("/dataset/stage/246")
        get_csrf_token(response)
    
    @task
    def dataset_unstage(self):
        response = self.client.post("/dataset/unstage/246")
        get_csrf_token(response)

    @task
    def stage_all(self):
        response = self.client.post("/dataset/stage/all")
        get_csrf_token(response)
    
    @task
    def unstage_all(self):
        response = self.client.post("/dataset/unstage/all")
        get_csrf_token(response)

    @task
    def publish_dataset(self):
        response = self.client.post("/dataset/publish")
        get_csrf_token(response)
class DatasetUser(HttpUser):
    tasks = [DatasetBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
