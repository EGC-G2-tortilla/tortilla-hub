import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def wait_for_page_to_load(driver, timeout=10):
    """Espera a que la página esté completamente cargada."""
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def validate_profile(driver, url, is_self=True):
    """
    Valida los elementos de un perfil dado (usuario autenticado o de otro usuario).
    """
    # Navega a la URL del perfil
    driver.get(url)
    time.sleep(3)

    print(f"Validando perfil en {url}...")

    # Nombre
    name_element = driver.find_element(
        By.XPATH, "//p[contains(@class, 'card-text') and contains(., 'Name:')]"
    )
    name_text = name_element.text
    assert (
        "Name:" in name_text and name_text.split(":")[1].strip() != ""
    ), "Test failed! Name not found."

    # Apellido
    surname_element = driver.find_element(
        By.XPATH, "//p[contains(@class, 'card-text') and contains(., 'Surname:')]"
    )
    surname_text = surname_element.text
    assert (
        "Surname:" in surname_text and surname_text.split(":")[1].strip() != ""
    ), "Test failed! Surname not found."

    # Afiliación
    affiliation_element = driver.find_element(
        By.XPATH, "//p[contains(@class, 'card-text') and contains(., 'Affiliation:')]"
    )
    affiliation_text = affiliation_element.text
    assert (
        "Affiliation:" in affiliation_text
        and affiliation_text.split(":")[1].strip() != ""
    ), "Test failed! Affiliation not found."

    # Email
    email_element = driver.find_element(
        By.XPATH, "//p[contains(@class, 'card-text') and contains(., 'Email:')]"
    )
    email_text = email_element.text
    assert (
        "Email:" in email_text and email_text.split(":")[1].strip() != ""
    ), "Test failed! Email not found."

    # Número de datasets
    datasets_element = driver.find_element(
        By.XPATH,
        "//p[contains(@class, 'card-text') and contains(., 'Uploaded datasets:')]",
    )
    datasets_text = datasets_element.text
    assert (
        "Uploaded datasets:" in datasets_text
        and datasets_text.split(":")[1].strip() != ""
    ), "Test failed! Datasets info not found."

    print(
        f"Perfil validado para {'usuario actual' if is_self else 'otro usuario'} exitosamente!"
    )
    print(
        f"Nombre: {name_text}, Apellido: {surname_text}, Afiliación: {affiliation_text}, "
        f"Email: {email_text}, Datasets: {datasets_text}"
    )


def test_view_my_profile():
    """
    Test para validar el perfil del usuario autenticado.
    """
    driver = initialize_driver()
    try:
        host = get_host_for_selenium_testing()

        # Login
        driver.get(f"{host}/login")
        time.sleep(3)
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)

        # Valida el perfil del usuario autenticado
        validate_profile(driver, f"{host}/profile/summary", is_self=True)

    except Exception as e:
        print(f"Error durante la prueba: {e}")
        with open("debug_page_source.html", "w") as f:
            f.write(driver.page_source)
        raise

    finally:
        close_driver(driver)


def test_view_other_user_profile():
    """
    Test para validar el perfil de otro usuario.
    """
    driver = initialize_driver()
    try:
        host = get_host_for_selenium_testing()

        # Login
        driver.get(f"{host}/login")
        time.sleep(3)
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)

        # Valida el perfil de otro usuario (e.g., user con ID 2)
        validate_profile(driver, f"{host}/profile/summary/2", is_self=False)

    except Exception as e:
        print(f"Error durante la prueba: {e}")
        with open("debug_page_source.html", "w") as f:
            f.write(driver.page_source)
        raise

    finally:
        close_driver(driver)


# Llama a las funciones de prueba
test_view_my_profile()
test_view_other_user_profile()
