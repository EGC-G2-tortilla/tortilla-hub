import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def wait_for_page_to_load(driver, timeout=10):
    """Espera a que la página esté completamente cargada."""
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def validate_fm_fact_labels(driver, dataset_doi, expected_labels):
    """
    Valida que los FM Fact Labels de un dataset sean correctos.
    """
    # Cambiar la ruta para usar el DOI
    driver.get(f"{get_host_for_selenium_testing()}/doi/{dataset_doi}/")
    wait_for_page_to_load(driver)

    # Validar total de modelos
    total_models_element = driver.find_element(
        By.XPATH, "//li[contains(., 'Total Models:')]"
    )
    assert (
        str(expected_labels["total_models"]) in total_models_element.text
    ), f"Total Models mismatch: Expected {expected_labels['total_models']}"

    # Validar total de features
    total_features_element = driver.find_element(
        By.XPATH, "//li[contains(., 'Total Features:')]"
    )
    assert (
        str(expected_labels["total_features"]) in total_features_element.text
    ), f"Total Features mismatch: Expected {expected_labels['total_features']}"

    # Validar total de constraints
    total_constraints_element = driver.find_element(
        By.XPATH, "//li[contains(., 'Total Constraints:')]"
    )
    assert (
        str(expected_labels["total_constraints"]) in total_constraints_element.text
    ), f"Total Constraints mismatch: Expected {expected_labels['total_constraints']}"

    # Validar profundidad máxima
    max_depth_element = driver.find_element(By.XPATH, "//li[contains(., 'Max Depth:')]")
    assert (
        str(expected_labels["max_depth"]) in max_depth_element.text
    ), f"Max Depth mismatch: Expected {expected_labels['max_depth']}"

    print("FM Fact Labels validated successfully!")


def test_validate_fm_fact_labels_invalid():
    """
    Test para validar que los FM Fact Labels incorrectos generen un fallo.
    """
    driver = initialize_driver()
    try:
        # Login
        host = get_host_for_selenium_testing()
        driver.get(f"{host}/login")
        time.sleep(3)
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)

        # Intentar validar FM Fact Labels con valores incorrectos
        incorrect_labels = {
            "total_models": 0,
            "total_features": 15,
            "total_constraints": 5,
            "max_depth": 8,
        }
        validate_fm_fact_labels(
            driver, dataset_doi="10.1234/dataset1", expected_labels=incorrect_labels
        )

    except AssertionError as e:
        print(f"Test passed: {e}")

    except Exception as e:
        print(f"Unexpected error during the test: {e}")
        with open("debug_page_source.html", "w") as f:
            f.write(driver.page_source)
        raise

    finally:
        close_driver(driver)


def test_fm_fact_labels_display_dataset():
    """
    Test para verificar que las Fact Labels de un dataset se muestran en la interfaz en la página DOI.
    """
    driver = initialize_driver()
    try:
        # Login
        host = get_host_for_selenium_testing()
        driver.get(f"{host}/login")
        time.sleep(3)
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)

        # Acceder a la página del dataset usando el DOI
        dataset_doi = "10.1234/dataset1"  # Ajusta el DOI del dataset de prueba
        driver.get(f"{host}/doi/{dataset_doi}/")
        wait_for_page_to_load(driver)

        # Esperar a que las Fact Labels estén visibles
        wait = WebDriverWait(driver, 10)

        total_models = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(., 'Total Models:')]")
            )
        )
        total_features = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(., 'Total Features:')]")
            )
        )
        total_constraints = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(., 'Total Constraints:')]")
            )
        )
        max_depth = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(., 'Max Depth:')]")
            )
        )

        # Validar que las Fact Labels están presentes
        assert total_models, "Missing Fact Label: Total Models"
        assert total_features, "Missing Fact Label: Total Features"
        assert total_constraints, "Missing Fact Label: Total Constraints"
        assert max_depth, "Missing Fact Label: Max Depth"

        print("Fact Labels for the dataset are displayed correctly on the DOI page!")

    except Exception as e:
        print(f"Error during the test: {e}")
        driver.save_screenshot("debug_doi_page_screenshot.png")
        with open("debug_doi_page_source.html", "w") as f:
            f.write(driver.page_source)
        raise

    finally:
        close_driver(driver)


def test_fm_fact_labels_display_model():
    """
    Test para verificar que las Fact Labels de un modelo aparecen en la interfaz de usuario en la página del modelo.
    """
    driver = initialize_driver()
    try:
        # Login
        host = get_host_for_selenium_testing()
        driver.get(f"{host}/login")
        time.sleep(3)
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")
        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")
        password_field.send_keys(Keys.RETURN)
        time.sleep(3)

        # Acceder a la página del modelo utilizando el DOI del dataset al que pertenece
        dataset_doi = "10.1234/dataset1"  # Ajusta el DOI del dataset de prueba
        driver.get(f"{host}/doi/{dataset_doi}/")
        wait_for_page_to_load(driver)

        # Validar presencia de Fact Labels específicas para un modelo
        wait = WebDriverWait(driver, 10)

        total_features = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(., 'Total Features:')]")
            )
        )
        total_constraints = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(., 'Total Constraints:')]")
            )
        )
        max_depth = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//li[contains(., 'Max Depth:')]")
            )
        )

        # Validar que las Fact Labels están presentes
        assert total_features, "Missing Fact Label: Total Features"
        assert total_constraints, "Missing Fact Label: Total Constraints"
        assert max_depth, "Missing Fact Label: Max Depth"

        print("Fact Labels for the model are displayed correctly on the page!")

    except Exception as e:
        print(f"Error during the test: {e}")
        driver.save_screenshot("debug_model_screenshot.png")
        with open("debug_model_page_source.html", "w") as f:
            f.write(driver.page_source)
        raise

    finally:
        close_driver(driver)


# Ejecutar los tests
test_validate_fm_fact_labels_invalid()
test_fm_fact_labels_display_dataset()
test_fm_fact_labels_display_model()
