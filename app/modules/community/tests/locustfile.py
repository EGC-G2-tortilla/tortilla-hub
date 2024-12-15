from locust import HttpUser, TaskSet, task
from core.environment.host import get_host_for_locust_testing


class CommunityBehavior(TaskSet):
    def on_start(self):
        self.index()

    @task
    def index(self):
        response = self.client.get("/community")

        if response.status_code != 200:
            print(f"Community index failed: {response.status_code}")

    @task
    def community_view(self):
        response = self.client.get("/community/Super%20Important%20Community")

        if response.status_code != 200:
            print(f"Community view failed: {response.status_code}")

    @task
    def community_info(self):
        response = self.client.get("/community/Super%20Important%20Community/info")

        if response.status_code != 200:
            print(f"Community info failed: {response.status_code}")

    @task
    def community_members(self):
        response = self.client.get("/community/Super%20Important%20Community/members")

        if response.status_code != 200:
            print(f"Community members failed: {response.status_code}")

    @task
    def community_create(self):
        response = self.client.get("/community/create")

        if response.status_code != 200:
            print(f"Community create GET view failed: {response.status_code}")


class CommunityUser(HttpUser):
    tasks = [CommunityBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
