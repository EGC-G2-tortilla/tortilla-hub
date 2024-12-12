from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from core.environment.host import get_host_for_selenium_testing
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from core.selenium.common import initialize_driver, close_driver
from selenium.common.exceptions import NoSuchElementException


def wait_for_page_to_load(driver, timeout=4):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


SAMPLE_DATASET_ROUTE = "/doi/10.1234/dataset1/"  # Route for Sample Dataset 1


def test_exists_button():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        # Get the number of models in the dataset

        # 1. Ir a la página de login
        # Navigate to the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # 2. Ir la página de un sataset
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Obtener el botón de subir archivo
        upload_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "uploadButton"))
        )
        # Verificar si el botón es visible y habilitado
        assert (
            upload_button.is_displayed() and upload_button.is_enabled()
        ), "El botón no está visible o habilitado"

        # Desplazarse al elemento
        driver.execute_script("arguments[0].scrollIntoView(true);", upload_button)

        assert driver.find_element(
            By.ID, "uploadButton"
        ), "El botón de subir archivo no existe"
    finally:
        close_driver(driver)


def test_not_exists_button():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        # Ir a la página de un dataset
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        try:
            driver.find_element(By.ID, "uploadButton")
            assert False, "El botón de subir archivo existe"
        except NoSuchElementException:
            assert (
                True  # El botón no se encontró, lo cual es el comportamiento esperado
            )
    finally:
        close_driver(driver)
