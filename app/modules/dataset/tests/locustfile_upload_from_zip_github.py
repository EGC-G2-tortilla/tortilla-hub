from locust import TaskSet, task, between, HttpUser
from core.environment.host import get_host_for_locust_testing
from core.locust.common import get_csrf_token
from zipfile import ZipFile


class UploadZipBehavior(TaskSet):
    def on_start(self):
        """Simula el inicio de sesión antes de cualquier tarea."""
        self.login()

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
                    if response.status_code == 200:
                        response.success()
                    else:
                        response.failure("Login failed")
            else:
                response.failure("Failed to get CSRF token")

    @task(1)
    def upload_from_zip(self):
        """Simula la subida de un dataset desde un archivo ZIP."""
        # Crear un archivo ZIP válido
        zip_filename = "dataset.zip"
        with ZipFile(zip_filename, "w") as zipf:
            zipf.writestr("file1.uvl", "This is the content of file1")
            zipf.writestr("file2.uvl", "This is the content of file2")

        # Subir el archivo ZIP
        with open(zip_filename, "rb") as f:
            upload_data = {
                "zipFile": (zip_filename, f, "application/zip"),
            }
            with self.client.post(
                "/dataset/upload_zip/1",
                files=upload_data,
                name="Upload Dataset",
                catch_response=True,
            ) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(
                        f"Failed to upload dataset: {response.status_code}, {response.text}"
                    )


class UploadGitHubFilesBehavior(TaskSet):
    def on_start(self):
        """Simula el inicio de sesión antes de realizar cualquier tarea."""
        self.login()

    @task(1)
    def upload_github_files(self):
        """Simula el envío de la URI del repositorio para obtener archivos UVL."""
        repo_url = "https://github.com/EGC-G2-tortilla/tortilla-hub.git"
        print(f"Enviado repo_url: {repo_url}")

        with self.client.post(
            "/dataset/download_repo_zip",
            data={"repo_url": repo_url},
            catch_response=True,
        ) as response:
            print("=== GitHub Repo URI Response Debug ===")
            print("Status Code:", response.status_code)
            print("Headers:", response.headers)
            print("Body (truncated):", response.text[:500])
            print("===============================")

            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to upload GitHub repo URL")

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
                    if response.status_code == 200:
                        response.success()
                    else:
                        response.failure("Login failed: Expected content not found")
            else:
                print("Failed to retrieve CSRF token. Response body:")
                print(response.text)
                raise ValueError("CSRF token not found")


class SelectAndUploadFilesBehavior(TaskSet):
    def on_start(self):
        """Simula el inicio de sesión antes de realizar cualquier tarea."""
        self.login()

    @task(1)
    def select_and_upload_files(self):
        """Simula la selección y subida de archivos UVL."""
        # Simula una lista de archivos UVL seleccionados
        dataset_id = "1"
        selected_files = ["file1.uvl", "file2.uvl"]

        print(f"Seleccionando archivos para dataset {dataset_id}: {selected_files}")

        with self.client.post(
            "/dataset/upload_github_files",
            data={"dataset_id": dataset_id, "files": selected_files},
            catch_response=True,
        ) as response:
            print("=== Upload Files Response Debug ===")
            print("Status Code:", response.status_code)
            print("Headers:", response.headers)
            print("Body (truncated):", response.text[:500])
            print("===============================")

            if response.status_code == 200:
                response.success()
            else:
                response.failure("Failed to upload selected files")

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
                    if response.status_code == 200:
                        response.success()
                    else:
                        response.failure("Login failed: Expected content not found")
            else:
                print("Failed to retrieve CSRF token. Response body:")
                print(response.text)
                raise ValueError("CSRF token not found")


class UploadGitHubUser(HttpUser):
    tasks = [UploadGitHubFilesBehavior, SelectAndUploadFilesBehavior]
    wait_time = between(5, 9)
    host = get_host_for_locust_testing()


class UploadZipUser(HttpUser):
    tasks = [UploadZipBehavior]
    host = get_host_for_locust_testing()
    wait_time = between(1, 2)
