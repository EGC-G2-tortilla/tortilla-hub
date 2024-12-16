import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from core.selenium.common import initialize_driver, close_driver
import os

load_dotenv()

# Obtener las credenciales de Discord desde el archivo .env
username = os.getenv("CREDENTIALS_USERNAME")
password = os.getenv("CREDENTIALS_PASSWORD")


def wait_for_page_to_load(driver, timeout=10):
    """
    Espera a que la página termine de cargar completamente.
    """
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def scroll_to_top(driver):
    """
    Desplaza hacia arriba en la página utilizando JavaScript.
    """
    driver.execute_script("window.scrollTo(0, 0);")


def wait_for_either_condition(driver, timeout, conditions):
    """
    Espera a que una de las condiciones se cumpla (en lugar de ambas al mismo tiempo).
    """
    return WebDriverWait(driver, timeout).until(
        lambda d: next(
            (
                d.find_element(*condition)
                for condition in conditions
                if d.find_elements(*condition)
            ),
            None,
        )
    )


def test_discord_bot_commands():
    """
    Test para verificar que el bot responde correctamente a los slash commands en Discord.
    """
    driver = initialize_driver()

    try:
        driver.get("https://tortilla-hub-development.onrender.com/")
        wait_for_page_to_load(driver)

        driver.get("https://discord.com/login")
        wait_for_page_to_load(driver)

        email_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(10)

        server_url = (
            "https://discord.com/channels/1317900109542985738/1317900109542985741"
        )
        driver.get(server_url)
        wait_for_page_to_load(driver)

        if len(driver.window_handles) == 0:
            raise Exception("La ventana se ha cerrado antes de completar el test.")

        # Crear el canal de prueba
        create_channel_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@class='addButton_a08117 forceVisible_a08117 button_dd4f85 lookBlank_dd4f85 "
                    "colorBrand_dd4f85 grow_dd4f85']",
                )
            )
        )

        create_channel_button.click()

        channel_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//input[@class='inputDefault_f8bc55 input_f8bc55 inputInner_b545d5']",
                )
            )
        )

        channel_name_field.send_keys("testing")
        channel_name_field.send_keys(Keys.RETURN)

        wait_for_page_to_load(driver)
        time.sleep(3)

        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='markup_f8f345 editor_a552a6 slateTextArea_e52116 fontSize16Padding_bdf0de']",
                )
            )
        )

        commands = [
            ("/help", "Ayuda del Bot"),
            ("/datasets_counter", "Total de Datasets Sincronizados"),
            ("/feature_models_counter", "Total de Modelos de Características"),
            ("/total_dataset_downloads", "Total de Descargas de Datasets"),
            (
                "/total_feature_model_downloads",
                "Total de Descargas de Modelos de Características",
            ),
            ("/total_dataset_views", "Total de Descargas de Datasets"),
            (
                "/total_feature_model_views",
                "Total de Vistas de Modelos de Características",
            ),
            ("/datasets", "Dataset"),
            ("/most_popular_authors", "Autores Más Populares"),
            ("/most_downloaded", "Gráfico de descargas"),
        ]

        for command, expected_text in commands:
            message_box.send_keys(command)
            time.sleep(0.5)
            if command == "/datasets":
                message_box.send_keys(Keys.DOWN)
                time.sleep(0.5)
            message_box.send_keys(Keys.RETURN)
            time.sleep(0.5)
            message_box.send_keys(Keys.RETURN)

            if command == "/most_downloaded":
                response_message = wait_for_either_condition(
                    driver,
                    timeout=10,
                    conditions=[
                        (
                            By.XPATH,
                            f"//div[@class='embedTitle_b0068a embedMargin_b0068a']"
                            f"//span[contains(text(), '{expected_text}')]",
                        ),
                        (
                            By.XPATH,
                            "//div[@class='embedTitle_b0068a embedMargin_b0068a']"
                            "//span[contains(text(), 'Sin datos disponibles')]",
                        ),
                    ],
                )

            elif command == "/most_popular_authors":
                response_message = wait_for_either_condition(
                    driver,
                    timeout=10,
                    conditions=[
                        (
                            By.XPATH,
                            f"//div[@class='embedTitle_b0068a embedMargin_b0068a']"
                            f"//span[contains(text(), '{expected_text}')]",
                        ),
                        (
                            By.XPATH,
                            "//span[contains(text(), 'No hay datos sobre autores populares en este momento')]",
                        ),
                    ],
                )
            else:
                response_message = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            f"//div[@class='embedTitle_b0068a embedMargin_b0068a']"
                            f"//span[contains(text(), '{expected_text}')]",
                        )
                    )
                )
            print(f"Bot respondió correctamente: {response_message.text}")

            time.sleep(2)

        scroll_to_top(driver)

        options_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@class='button_ccfa44 button_dd4f85 lookBlank_dd4f85 colorBrand_dd4f85 sizeMin_dd4f85 "
                    "grow_dd4f85']",
                )
            )
        )
        options_button.click()
        wait_for_page_to_load(driver)

        delete_channel_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='item_a0 themed_a0'][@aria-label='Eliminar canal']",
                )
            )
            or EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//div[@class='item_a0 themed_a0'][@aria-label='Delete channel']",
                )
            )
        )
        delete_channel_button.click()
        wait_for_page_to_load(driver)

        confirm_delete_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@class='button_dd4f85 lookFilled_dd4f85 colorRed_dd4f85 sizeMedium_dd4f85 grow_dd4f85']",
                )
            )
        )

        confirm_delete_button.click()
        time.sleep(2)

    except Exception as e:
        print(f"Se produjo un error: {str(e)}")
    finally:
        # Cerrar el navegador
        close_driver(driver)


if __name__ == "__main__":
    test_discord_bot_commands()
