import unittest
from selenium.webdriver.common.by import By
from app.modules.auth.tests.test_selenium import wait_for_page_to_load
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


class TestHomePage(unittest.TestCase):
    def test_home_page_text(self):
        driver = initialize_driver()

        try:
            host = get_host_for_selenium_testing()

            # Open the main page
            driver.get(f"{host}/")
            wait_for_page_to_load(driver)

            expected_text = """¡Felices fiestas! 🎉 Desde el equipo de *tortilla-hub* queremos desearles unas fiestas llenas de alegría, comida rica y momentos inolvidables con sus familias y amigos. Que el espíritu navideño les traiga no solo turrones y polvorones, sino también mucha suerte y energía para el próximo año. Y, por supuesto, esperamos que los Reyes Magos (o Papá Noel, no discriminamos a nadie 😉) vengan cargados de *buenas notas*, porque al carbón ya le tenemos suficiente respeto en la barbacoa. ¡A disfrutar y a recargar pilas para lo que viene! 🎄✨"""

            # Locate the element
            element = driver.find_element(By.XPATH, "//div[@class='card-body card-body-slim']")

            # Assertions
            self.assertEqual(element.text, expected_text)
            self.assertTrue(element.is_displayed(), "Popular datasets chart not displayed!")

            print("Data display test passed! Merry Christmas!")

        finally:
            # Close the browser
            close_driver(driver)


unittest.main()