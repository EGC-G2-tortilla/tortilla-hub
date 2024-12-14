import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
from core.selenium.common import initialize_driver, close_driver
import os

# Cargar las variables de entorno
load_dotenv()

# Obtener las credenciales de Discord desde el archivo .env
username = os.getenv("DISCORD_USERNAME")
password = os.getenv("DISCORD_PASSWORD")


def wait_for_page_to_load(driver, timeout=10):
    """
    Espera a que la página termine de cargar completamente.
    """
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def test_discord_bot_command_help():
    """
    Test para verificar que el bot responde correctamente a un slash command help en Discord.
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

        server_url = "https://discord.com/channels/1313534413082071140/1317455188025413643"
        driver.get(server_url)
        wait_for_page_to_load(driver)

        if len(driver.window_handles) == 0:
            raise Exception("La ventana se ha cerrado antes de completar el test.")

        # Paso 4: Encontrar el campo de entrada para enviar un comando
        message_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Enviar mensaje a #testing']"))
        )

        slash_command = "/help"
        message_box.send_keys(slash_command)
        message_box.send_keys(Keys.RETURN)
        message_box.send_keys(Keys.RETURN)

        response_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//div[@class='embedTitle_b0068a embedMargin_b0068a']//span[contains(text(), 'Ayuda del Bot')]"
            ))
        )
        print("Bot respondió correctamente:", response_message.text)

        # actions = ActionChains(driver)
        # actions.move_to_element(response_message).perform()

        # # Paso 7: Esperar y hacer clic en el botón de tres puntos
        # try:
        #     three_dots_button = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((
        #             By.XPATH,
        #             "//div[@class='hoverBarButton_e986d9 button_f7e168 selected_f7e168']"
        #         ))
        #     )
        #     three_dots_button.click()
        # except Exception as e:
        #     print("Error al encontrar o hacer clic en el botón de tres puntos:", e)

        # # Paso 8: Esperar y hacer clic en "Eliminar"
        # delete_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((
        #         By.XPATH,
        #         "//button[@aria-label='Eliminar']"
        #     ))
        # )
        # delete_button.click()

        # time.sleep(2)  # Esperar a que aparezca

        # # Paso 10: Confirmar la eliminación del mensaje
        # confirm_delete_button = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((
        #         By.XPATH,
        #         "//button[@type='submit' and contains(text(), 'Eliminar')]"
        #     ))
        # )
        # confirm_delete_button.click()

    except Exception as e:
        print(f"Se produjo un error: {str(e)}")
    finally:
        # Cerrar el navegador
        close_driver(driver)


# Ejecutar el test
if __name__ == "__main__":
    test_discord_bot_command_help()
