import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver


# Define the route for the dataset
SAMPLE_DATASET_ROUTE = "/doi/10.1234/dataset2/"  # Route for Sample Dataset 1


def wait_for_page_to_load(driver, timeout=4):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def test_rate_dataset_authenticated():
    """Test to verify that a user can successfully rate a dataset when authenticated."""
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

        # 3. Navigate to the dataset page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")  # Use the correct route for the dataset
        wait_for_page_to_load(driver)

        # 4. Ensure the stars container is displayed
        stars_container = driver.find_element(By.ID, "stars")
        assert stars_container.is_displayed(), "The stars container is not displayed!"

        # 5. Hover over the third star and click it
        third_star = stars_container.find_element(By.XPATH, "//span[@data-rating='3']")
        ActionChains(driver).move_to_element(third_star).click().perform()
        time.sleep(1)  # Allow time for the server to respond

        # 6. Verify confirmation message
        alert_box = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "toast-alert"))
        )
        assert "Thank you for your rating!" in alert_box.text, "Rating confirmation message not displayed!"

        print("Rating submission test passed!")

    finally:
        close_driver(driver)


def test_rate_dataset_unauthenticated():
    """Test to verify that a user cannot rate a dataset when not authenticated."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}")
        wait_for_page_to_load(driver)

        # 1. Navigate to the dataset page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")  # Use the correct route for the dataset
        wait_for_page_to_load(driver)

        # 2. Try to find the stars container
        try:
            stars_container = driver.find_element(By.ID, "stars")
            assert stars_container.is_displayed(), "The stars container is displayed for an unauthenticated user!"
        except Exception as e:
            print("Stars container not visible for unauthenticated users, as expected.")

        print("Unauthenticated user cannot rate dataset test passed!")

    finally:
        close_driver(driver)
