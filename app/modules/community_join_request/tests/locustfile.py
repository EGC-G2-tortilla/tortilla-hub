from locust import HttpUser, TaskSet, task
from core.environment.host import get_host_for_locust_testing


class CommunityJoinRequestBehavior(TaskSet):
    def on_start(self):
        self.index()

    @task
    def index(self):
        response = self.client.get("/community_join_request")

        if response.status_code != 200:
            print(f"CommunityJoinRequest index failed: {response.status_code}")


class CommunityJoinRequestUser(HttpUser):
    tasks = [CommunityJoinRequestBehavior]
    min_wait = 5000
    max_wait = 9000
    host = get_host_for_locust_testing()
