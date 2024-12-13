from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
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
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
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
        download_zip_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "downloadZipForm"))
        )
        repo_url_input = driver.find_element(By.ID, "repoUrlInput")
        download_zip_button = download_zip_form.find_element(By.ID, "downloadZipButton")

        # 6. Llenar el campo de URL del repositorio
        repo_url_input.send_keys("https://github.com/rafpulcif/uvlhub.git")

        # 7. Hacer clic en el botón "Upload from Github"
        try:
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "downloadZipButton"))
            ).click()
        except ElementClickInterceptedException:
            driver.execute_script("arguments[0].scrollIntoView(true);", download_zip_button)
            download_zip_button.click()

        # 8. Verificar que el modal se muestra correctamente
        github_modal = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "githubModal"))
        )
        assert github_modal.is_displayed(), "El modal de GitHub no se mostró correctamente."

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
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
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
        download_zip_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "downloadZipForm"))
        )
        repo_url_input = driver.find_element(By.ID, "repoUrlInput")
        download_zip_button = download_zip_form.find_element(By.ID, "downloadZipButton")

        # 6. Llenar el campo de URL del repositorio con una URL no válida
        repo_url_input.send_keys("https://github.com/rafpulcif/uvlhub")

        # 7. Hacer clic en el botón "Upload from Github"
        try:
            download_zip_button.click()
        except ElementClickInterceptedException:
            assert True
        else:
            assert False, "No se lanzó ninguna excepción al hacer clic en el botón."
    finally:
        close_driver(driver)


def test_input_exists():
    driver = initialize_driver()
    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}")
        wait_for_page_to_load(driver)

        # 1. Ir a inicio de sesión
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # 2. Enter the email address and password
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
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
        download_zip_form = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "downloadZipForm"))
        )
        download_zip_button = download_zip_form.find_element(By.ID, "downloadZipButton")

        # 6. Asertar que el botón existe y el form
        assert download_zip_form is not None
        assert download_zip_button is not None
    finally:
        close_driver(driver)


def test_input_not_exists():
    driver = initialize_driver()
    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}")
        wait_for_page_to_load(driver)

        # 1. Ir a la página del dataset
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # 2. Hacer scroll al final de la página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 3. Verificar que el formulario y el botón no existen
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, "downloadZipForm"))
            )
            assert False, "El formulario no debería existir, pero se encontró."
        except TimeoutException:
            assert True
    finally:
        close_driver(driver)
