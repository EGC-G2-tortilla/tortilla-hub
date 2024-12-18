from locust import HttpUser, TaskSet, task, between
from core.locust.common import get_csrf_token, fake


class AuthBehavior(TaskSet):
    def on_start(self):
        # Opcional: Realiza alguna acción antes de iniciar las tareas
        self.ensure_logged_out()

    @task(2)
    def signup(self):
        response = self.client.get("/signup")
        csrf_token = get_csrf_token(response)
        response = self.client.post(
            "/signup",
            data={
                "email": fake.email(),
                "password": fake.password(),
                "csrf_token": csrf_token,
            },
        )
        if response.status_code != 200:
            print(f"Signup failed: {response.status_code}")

    @task(2)
    def login(self):
        response = self.client.get("/login")
        csrf_token = get_csrf_token(response)
        response = self.client.post(
            "/login",
            data={
                "email": "user1@example.com",
                "password": "1234",
                "csrf_token": csrf_token,
            },
        )
        if response.status_code != 200:
            print(f"Login failed: {response.status_code}")

    @task(1)
    def signup_google(self):
        response = self.client.get("/signup/google")
        if response.status_code == 302:
            redirect_url = response.headers.get("Location", "")
            if "accounts.google.com" in redirect_url:
                response = self.client.post(redirect_url)
                if response.status_code == 200:
                    print("Signup con Google completado.")
                else:
                    print(f"Signup con Google fallido: {response.status_code}")

    @task(1)
    def login_google(self):
        response = self.client.get("/login/google")
        if response.status_code == 302:
            redirect_url = response.headers.get("Location", "")
            if "accounts.google.com" in redirect_url:
                response = self.client.post(redirect_url)
                if response.status_code == 200:
                    print("Login con Google completado.")
                else:
                    print(f"Login con Google fallido: {response.status_code}")

    @task(1)
    def signup_orcid(self):
        response = self.client.get("/signup/orcid")
        if response.status_code == 302:
            redirect_url = response.headers.get("Location", "")
            if "orcid.org" in redirect_url:
                print("Signup con ORCID redirige correctamente.")
            else:
                print(f"Unexpected redirect during ORCID signup: {redirect_url}")

    @task(1)
    def login_orcid(self):
        response = self.client.get("/login/orcid")
        if response.status_code == 302:
            redirect_url = response.headers.get("Location", "")
            if "orcid.org" in redirect_url:
                print("Login con ORCID redirige correctamente.")
            else:
                print(f"Unexpected redirect during ORCID login: {redirect_url}")

    @task(1)
    def signup_github(self):
        self.client.cookies.clear()
        response = self.client.get("/signup/github")
        if response.status_code == 302:
            redirect_url = response.headers.get("Location", "")
            if "github.com" in redirect_url:
                print("Signup con GitHub redirige correctamente.")
            else:
                print(f"Unexpected redirect during GitHub signup: {redirect_url}")
        else:
            print(f"Signup con GitHub fallido: {response.status_code}")

    @task(1)
    def login_github(self):
        self.client.cookies.clear()
        response = self.client.get("/login/github")
        if response.status_code == 302:
            redirect_url = response.headers.get("Location", "")
            if "github.com" in redirect_url:
                print("Login con GitHub redirige correctamente.")
            else:
                print(f"Unexpected redirect during GitHub login: {redirect_url}")
        else:
            print(f"Login con GitHub fallido: {response.status_code}")

    def ensure_logged_out(self):
        self.client.cookies.clear()
        self.client.get("/logout")


class AuthUser(HttpUser):
    tasks = [AuthBehavior]
    wait_time = between(0.5, 2)  # Tiempo de espera entre tareas
    host = "https://tortilla-hub-production.onrender.com"
