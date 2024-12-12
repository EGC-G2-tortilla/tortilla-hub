import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver


def wait_for_page_to_load(driver, timeout=4):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def test_download_all_authenticated():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}")
        wait_for_page_to_load(driver)

        # 1. Click on the "Login" button
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # 2. Enter the email address and password
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # 3. Vuelta a la página principal
        driver.get(f"{host}")
        wait_for_page_to_load(driver)

        # 4. Click on the "Download all" button
        # Esperar explícitamente a que el elemento sea clickable
        download_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a[href='/dataset/download_all']")
            )
        )

        # Verificar si el botón es visible y habilitado
        assert (
            download_button.is_displayed() and download_button.is_enabled()
        ), "El botón no está visible o habilitado"

        # Desplazarse al elemento
        driver.execute_script("arguments[0].scrollIntoView(true);", download_button)

        # Usar un clic a través de JavaScript para evitar problemas de intercepción
        try:
            driver.execute_script("arguments[0].click();", download_button)
        except Exception as e:
            raise RuntimeError(f"No se pudo hacer clic en el botón: {str(e)}")

        wait_for_page_to_load(driver)

        # 5. Check if in the response headers theres an X-Success-Message
        session_cookies = driver.get_cookies()
        cookies = {cookie["name"]: cookie["value"] for cookie in session_cookies}

        response = requests.get(f"{host}/dataset/download_all", cookies=cookies)

        assert (
            response.headers.get("X-Success-Message")
            == "All datasets downloaded successfully"
        ), "El encabezado 'X-Success-Message' no contiene el valor esperado en la respuesta"

    finally:
        close_driver(driver)


test_download_all_authenticated()
