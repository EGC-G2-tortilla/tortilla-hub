import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from dotenv import load_dotenv
from core.selenium.common import initialize_driver, close_driver
import os

load_dotenv()

# Credenciales generales
credentials_username = os.getenv("CREDENTIALS_USERNAME")
credentials_password = os.getenv("CREDENTIALS_PASSWORD")


def wait_for_page_to_load(driver, timeout=10):
    """
    Espera a que la página termine de cargar completamente.
    """
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def test_authorize_github_signup():
    """
    Test para verificar el flujo de autorización de GitHub en modo 'signup'.
    """
    driver = initialize_driver()

    try:
        # Paso 1: Navegar a la página de registro
        base_url = "https://tortilla-hub-production.onrender.com"  # Cambia según tu entorno
        driver.get(f"{base_url}/signup")
        wait_for_page_to_load(driver)

        # Paso 2: Hacer clic en el botón "Sign Up with GitHub"
        github_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//a[contains(@href, '/signup/github') and contains(., 'Sign Up with GitHub')]"
            ))
        )
        github_button.click()
        wait_for_page_to_load(driver)

        # Paso 3: Verificar redirección a GitHub
        WebDriverWait(driver, 10).until(
            EC.url_contains("github.com/login")
        )
        print("Redirección a GitHub exitosa")

        # Paso 4: Completar credenciales de GitHub
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(credentials_username)
        password_field.send_keys(credentials_password)
        password_field.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        print("Test del flujo 'signup' completado con éxito.")

    except TimeoutException as e:
        print(f"Error de tiempo de espera: {str(e)}")
    except Exception as e:
        print(f"Se produjo un error: {str(e)}")
    finally:
        # Cerrar el navegador
        close_driver(driver)


def test_authorize_github_login():
    """
    Test para verificar el flujo de autorización de GitHub en modo 'login'.
    """
    driver = initialize_driver()

    try:
        # Paso 1: Navegar a la página de registro
        base_url = "https://tortilla-hub-production.onrender.com"  # Cambia según tu entorno
        driver.get(f"{base_url}/login")
        wait_for_page_to_load(driver)

        # Paso 2: Hacer clic en el botón "Sign Up with GitHub"
        github_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((
                By.XPATH,
                "//a[contains(@href, '/login/github') and contains(., 'Sign In with GitHub')]"
            ))
        )
        github_button.click()
        wait_for_page_to_load(driver)

        # Paso 3: Verificar redirección a GitHub
        WebDriverWait(driver, 10).until(
            EC.url_contains("github.com/login")
        )
        print("Redirección a GitHub exitosa")

        # Paso 4: Completar credenciales de GitHub
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(credentials_username)
        password_field.send_keys(credentials_password)
        password_field.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        print("Test del flujo 'login' completado con éxito.")

    except TimeoutException as e:
        print(f"Error de tiempo de espera: {str(e)}")
    except Exception as e:
        print(f"Se produjo un error: {str(e)}")
    finally:
        # Cerrar el navegador
        close_driver(driver)


def test_authorize_orcid_signup():
    """
    Test para verificar el flujo de autorización de ORCID en modo 'signup'.
    """
    driver = initialize_driver()

    try:
        base_url = (
            "https://tortilla-hub-production.onrender.com"  # Cambia según tu entorno
        )
        driver.get(f"{base_url}/signup")
        wait_for_page_to_load(driver)

        github_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@href, '/signup/orcid') and contains(., 'Sign Up with ORCID')]",
                )
            )
        )
        github_button.click()
        wait_for_page_to_load(driver)

        WebDriverWait(driver, 10).until(EC.url_contains("orcid.org/signin"))
        print("Redirección a ORCID exitosa:", driver.current_url)

        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username-input"))
        )
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(credentials_username)
        password_field.send_keys(credentials_password)
        password_field.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "email"))
        )
        email_field.send_keys(credentials_username)
        email_field.send_keys(Keys.RETURN)

        wait_for_page_to_load(driver)
        time.sleep(3)

        print("Test del flujo 'signup' completado con éxito.")

    except TimeoutException as e:
        print(f"Error de tiempo de espera: {str(e)}")
    except Exception as e:
        print(f"Se produjo un error: {str(e)}")
    finally:
        # Cerrar el navegador
        close_driver(driver)


def test_authorize_orcid_login():
    """
    Test para verificar el flujo de autorización de ORCID en modo 'login'.
    """
    driver = initialize_driver()

    try:
        base_url = (
            "https://tortilla-hub-production.onrender.com"  # Cambia según tu entorno
        )
        driver.get(f"{base_url}/login")
        wait_for_page_to_load(driver)

        github_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//a[contains(@href, '/login/orcid') and contains(., 'Sign In with ORCID')]",
                )
            )
        )
        github_button.click()
        wait_for_page_to_load(driver)

        WebDriverWait(driver, 10).until(EC.url_contains("orcid.org/signin"))
        print("Redirección a ORCID exitosa:", driver.current_url)

        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "username-input"))
        )
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(credentials_username)
        password_field.send_keys(credentials_password)
        password_field.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        time.sleep(3)

        print("Test del flujo 'login' completado con éxito.")

    except TimeoutException as e:
        print(f"Error de tiempo de espera: {str(e)}")
    except Exception as e:
        print(f"Se produjo un error: {str(e)}")
    finally:
        # Cerrar el navegador
        close_driver(driver)


# Ejecutar el test
if __name__ == "__main__":
    test_authorize_github_signup()
    test_authorize_github_login()
    # test_authorize_orcid_signup()
    # test_authorize_orcid_login()
