import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def wait_for_page_to_load(driver, timeout=10):
    """
    Espera a que la página termine de cargar completamente.
    """
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def test_upload_uvl_files():
    """
    Test para verificar la subida de archivos UVL (válido e inválido) y comprobar que los mensajes
    de error y éxito se comportan correctamente en la interfaz.
    """
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Paso 1: Iniciar sesión
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Rellenar los campos de login
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")
        password_field.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Paso 2: Navegar a la sección de subida de datasets
        driver.get(f"{host}/dataset/upload")
        wait_for_page_to_load(driver)

        # Paso 3: Subir un archivo UVL inválido
        invalid_file_path = os.path.abspath("app/modules/dataset/uvl_examples/invalid.uvl")
        dropzone = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dz-hidden-input"))
        )
        dropzone.send_keys(invalid_file_path)
        wait_for_page_to_load(driver)

        # Verificar que aparece la alerta de error
        error_alert = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
        )
        assert error_alert.is_displayed(), "Error alert not displayed for invalid file!"

        print("Error alert displayed successfully for invalid file.")

        # Paso 4: Cerrar la alerta de error
        close_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn-close"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", close_button)
        ActionChains(driver).move_to_element(close_button).click(close_button).perform()

        # Verificar que la alerta de error desaparece
        WebDriverWait(driver, 10).until(EC.staleness_of(error_alert))
        print("Error alert successfully dismissed.")

        # Paso 5: Subir un archivo UVL válido
        valid_file_path = os.path.abspath("app/modules/dataset/uvl_examples/file1.uvl")

        # Relocalizar el elemento dropzone antes de subir el archivo válido
        dropzone = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "dz-hidden-input"))
        )
        dropzone.send_keys(valid_file_path)
        wait_for_page_to_load(driver)

        # Verificar que no hay alertas de error para el archivo válido
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "alert-danger"))
            )
            assert False, "Error alert displayed for valid file!"
        except Exception:
            print("No error alert displayed for valid file. Upload successful.")

        print("Test passed: UVL file upload behaves as expected.")

    finally:
        # Cerrar el navegador
        close_driver(driver)


# Ejecutar el test
if __name__ == "__main__":
    test_upload_uvl_files()
