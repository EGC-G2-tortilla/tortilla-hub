#from selenium.common.exceptions import NoSuchElementException
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def wait_for_page_to_load(driver, timeout=4):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

"""

def test_community_index():

    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the index page
        driver.get(f'{host}/community')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        try:

            pass

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)
"""


def test_join_community():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, "email")
        password_field = driver.find_element(By.NAME, "password")

        email_field.send_keys("user1@example.com")
        password_field.send_keys("1234")

        # Send the form
        password_field.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Open the upload dataset
        driver.get(f"{host}/community")
        wait_for_page_to_load(driver)

        # Find basic info and UVL model and fill values
        link = driver.find_element(By.LINK_TEXT, "Super Important Community")
        link.click()
        wait_for_page_to_load(driver)

        link = driver.find_element(By.NAME, "join_community_button")
        link.click()
        wait_for_page_to_load(driver)

        try:
            you_are_already_a_member = driver.find_element(By.CLASS_NAME, "you_are_already_a_member")
        except Exception:
            you_are_already_a_member = None

        assert you_are_already_a_member, "Test failed!"
        
        print("Test passed!")

    finally:

        # Close the browser
        close_driver(driver)


# Call the test function
test_join_community()
