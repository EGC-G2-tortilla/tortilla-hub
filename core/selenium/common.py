import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def initialize_driver():
    # Initializes the browser options
    options = webdriver.ChromeOptions()

    # Initialise the browser using WebDriver Manager
    driver_path = ChromeDriverManager().install()
    chromedriver_binary = os.path.join(os.path.dirname(driver_path), 'chromedriver')
    os.chmod(chromedriver_binary, 0o777)
    service = Service(chromedriver_binary)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def close_driver(driver):
    driver.quit()
