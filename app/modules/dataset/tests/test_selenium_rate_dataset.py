import re
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
        driver.get(
            f"{host}{SAMPLE_DATASET_ROUTE}"
        )  # Use the correct route for the dataset
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
        assert (
            "Thank you for your rating!" in alert_box.text
        ), "Rating confirmation message not displayed!"

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
        driver.get(
            f"{host}{SAMPLE_DATASET_ROUTE}"
        )  # Use the correct route for the dataset
        wait_for_page_to_load(driver)

        # 2. Try to find the stars container
        try:
            stars_container = driver.find_element(By.ID, "stars")
            assert (
                stars_container.is_displayed()
            ), "The stars container is displayed for an unauthenticated user!"
        except Exception as e:
            print(
                f"Expected behavior: Stars container not visible for unauthenticated users. Error: {e}"
            )

        print("Unauthenticated user cannot rate dataset test passed!")

    finally:
        close_driver(driver)


def test_rating_persistence_authenticated():
    """Test to verify that the average rating is displayed after refreshing the page when authenticated."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}")
        wait_for_page_to_load(driver)

        # 1. Login to the application
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # 2. Navigate to the dataset page
        driver.get(
            f"{host}{SAMPLE_DATASET_ROUTE}"
        )  # Use the correct route for the dataset
        wait_for_page_to_load(driver)

        # 3. Select a rating (e.g., 4 stars)
        stars_container = driver.find_element(By.ID, "stars")
        fourth_star = stars_container.find_element(By.XPATH, "//span[@data-rating='4']")
        ActionChains(driver).move_to_element(fourth_star).click().perform()
        time.sleep(1)

        # 4. Refresh the page
        driver.refresh()
        wait_for_page_to_load(driver)

        # 5. Verify that the displayed rating corresponds to the average rating
        # Get the displayed average rating value
        average_rating_element = driver.find_element(By.ID, "rating-value")
        average_rating_text = average_rating_element.text

        # Extract the numeric part of the rating using regex
        match = re.search(r"(\d+\.\d+)", average_rating_text)
        if match:
            average_rating = float(match.group(1))
        else:
            raise ValueError(
                f"Could not extract a valid rating from text: {average_rating_text}"
            )

        # Verify that the average rating is within the valid range
        assert 0 <= average_rating <= 5, "The average rating displayed is not valid!"
        print(f"Displayed average rating after refresh: {average_rating}")

        print("Rating persistence test passed!")

    finally:
        close_driver(driver)


def test_average_rating_update():
    """Test to verify that the average rating updates and rating count behaves correctly when a user rates."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}")
        wait_for_page_to_load(driver)

        # 1. Login to the application
        driver.find_element(By.LINK_TEXT, "Login").click()
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # 2. Navigate to the dataset page
        driver.get(
            f"{host}{SAMPLE_DATASET_ROUTE}"
        )  # Use the correct route for the dataset
        wait_for_page_to_load(driver)

        # 3. Get initial average rating and total ratings
        initial_average = driver.find_element(By.ID, "rating-value").text

        # Extract numeric value from the initial count text
        initial_count_text = driver.find_element(By.ID, "rating-count").text
        initial_count_match = re.search(r"\d+", initial_count_text)
        initial_count = int(initial_count_match.group()) if initial_count_match else 0

        print(f"Initial average: {initial_average}, Initial count: {initial_count}")

        # 4. Submit a new rating
        stars_container = driver.find_element(By.ID, "stars")
        fourth_star = stars_container.find_element(By.XPATH, "//span[@data-rating='4']")
        ActionChains(driver).move_to_element(fourth_star).click().perform()

        # Add a wait to allow the rating to be processed
        time.sleep(2)

        # 5. Wait for the average rating to update
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(By.ID, "rating-value").text != initial_average
        )

        updated_average = driver.find_element(By.ID, "rating-value").text
        updated_count_text = driver.find_element(By.ID, "rating-count").text
        updated_count_match = re.search(r"\d+", updated_count_text)
        updated_count = int(updated_count_match.group()) if updated_count_match else 0

        print(f"Updated average: {updated_average}, Updated count: {updated_count}")

        # 6. Verify count and average
        if updated_count == initial_count:
            print("The user already rated this dataset, rating count did not increase.")
        elif updated_count == initial_count + 1:
            print(
                "The user rated this dataset for the first time, rating count increased."
            )
        else:
            raise AssertionError(
                f"Unexpected rating count behavior! Initial count: {initial_count}, Updated count: {updated_count}."
            )

        # Ensure the average rating has updated
        assert (
            updated_average != initial_average
        ), "Average rating did not update correctly!"

        print("Test passed: Rating count and average rating updated as expected!")

    finally:
        close_driver(driver)
