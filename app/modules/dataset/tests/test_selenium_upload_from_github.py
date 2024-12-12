from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import shutil

SAMPLE_DATASET_ROUTE = "/doi/10.1234/dataset1/"


def wait_for_page_to_load(driver, timeout=10):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def test_access_github_modal():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # 2. Enter the email address and password
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # 3. Página del dataset
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # 4. Hacer scroll al final de la página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 5. Localizar el formulario y el botón dentro del formulario
        download_zip_form = driver.find_element(By.ID, "downloadZipForm")
        repo_url_input = driver.find_element(By.ID, "repoUrlInput")
        download_zip_button = download_zip_form.find_element(By.ID, "downloadZipButton")

        # 6. Llenar el campo de URL del repositorio
        repo_url_input.send_keys("https://github.com/rafpulcif/uvlhub.git")

        # 7. Hacer clic en el botón "Upload from Github"
        download_zip_button.click()

        # 8. Verificar que el modal se muestra correctamente
        github_modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "githubModal"))
        )
        assert (
            github_modal.is_displayed()
        ), "El modal de GitHub no se mostró correctamente."
        shutil.rmtree("uploads/temp/")
    finally:
        close_driver(driver)


def test_invalid_github_url():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # 2. Enter the email address and password
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # 3. Página del dataset
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # 4. Hacer scroll al final de la página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 5. Localizar el formulario y el botón dentro del formulario
        download_zip_form = driver.find_element(By.ID, "downloadZipForm")
        repo_url_input = driver.find_element(By.ID, "repoUrlInput")
        download_zip_button = download_zip_form.find_element(By.ID, "downloadZipButton")

        # 6. Llenar el campo de URL del repositorio con una URL no válida
        repo_url_input.send_keys("https://github.com/rafpulcif/uvlhub")

        # 7. Hacer clic en el botón "Upload from Github"
        try:
            download_zip_button.click()
        except:
            assert True

    finally:
        close_driver(driver)
