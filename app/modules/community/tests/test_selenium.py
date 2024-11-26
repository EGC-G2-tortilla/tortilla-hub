from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver
import os
import time

def wait_for_page_to_load(driver, timeout=4):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


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
            you_are_already_a_member = driver.find_element(
                By.CLASS_NAME, "you_are_already_a_member"
            )
        except Exception:
            you_are_already_a_member = None

        assert you_are_already_a_member, "Test failed!"

        print("Test passed!")

    finally:

        # Close the browser
        close_driver(driver)


def test_create_community():
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
        link = driver.find_element(By.CLASS_NAME, "create_community")
        link.click()
        wait_for_page_to_load(driver)

        name = driver.find_element(By.NAME, "name")
        description = driver.find_element(By.NAME, "description_info")
        url = driver.find_element(By.NAME, "url")

        name.send_keys("sample sample community")
        description.send_keys("sample sample description")
        url.send_keys("https://veryimportantorganization.org")

        # Send the form
        url.send_keys(Keys.RETURN)

        link = driver.find_element(By.LINK_TEXT, "sample sample community")
        link.click()
        wait_for_page_to_load(driver)
        print("Test passed!")

    finally:

        # Close the browser
        close_driver(driver)


def test_upload_dataset_to_community():
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
        driver.get(f"{host}/community/Super%20Important%20Community/")
        wait_for_page_to_load(driver)

        upload_dataset_button = driver.find_element(
            By.CLASS_NAME, "upload_dataset_button"
        )
        upload_dataset_button.click()

        possible_urls = {
            f"{host}/dataset/Super Important Community/upload",
            f"{host}/dataset/Super%20Important%20Community/upload"
        }
        assert driver.current_url in possible_urls, "Test failed!"

        # Find basic info and UVL model and fill values
        title_field = driver.find_element(By.NAME, "title")
        title_field.send_keys("Title")
        desc_field = driver.find_element(By.NAME, "desc")
        desc_field.send_keys("Description")
        tags_field = driver.find_element(By.NAME, "tags")
        tags_field.send_keys("tag1,tag2")

        # Add two authors and fill
        add_author_button = driver.find_element(By.ID, "add_author")
        add_author_button.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)
        add_author_button.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        name_field0 = driver.find_element(By.NAME, "authors-0-name")
        name_field0.send_keys("Author0")
        affiliation_field0 = driver.find_element(By.NAME, "authors-0-affiliation")
        affiliation_field0.send_keys("Club0")
        orcid_field0 = driver.find_element(By.NAME, "authors-0-orcid")
        orcid_field0.send_keys("0000-0000-0000-0000")

        name_field1 = driver.find_element(By.NAME, "authors-1-name")
        name_field1.send_keys("Author1")
        affiliation_field1 = driver.find_element(By.NAME, "authors-1-affiliation")
        affiliation_field1.send_keys("Club1")

        # Obtén las rutas absolutas de los archivos
        file1_path = os.path.abspath("app/modules/dataset/uvl_examples/file1.uvl")
        file2_path = os.path.abspath("app/modules/dataset/uvl_examples/file2.uvl")

        # Subir el primer archivo
        dropzone = driver.find_element(By.CLASS_NAME, "dz-hidden-input")
        dropzone.send_keys(file1_path)
        wait_for_page_to_load(driver)

        # Subir el segundo archivo
        dropzone = driver.find_element(By.CLASS_NAME, "dz-hidden-input")
        dropzone.send_keys(file2_path)
        wait_for_page_to_load(driver)

        # Add authors in UVL models
        show_button = driver.find_element(By.ID, "0_button")
        show_button.send_keys(Keys.RETURN)
        add_author_uvl_button = driver.find_element(By.ID, "0_form_authors_button")
        add_author_uvl_button.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        name_field = driver.find_element(By.NAME, "feature_models-0-authors-2-name")
        name_field.send_keys("Author3")
        affiliation_field = driver.find_element(
            By.NAME, "feature_models-0-authors-2-affiliation"
        )
        affiliation_field.send_keys("Club3")

        # Check I agree and send form
        check = driver.find_element(By.ID, "agreeCheckbox")
        check.send_keys(Keys.SPACE)
        wait_for_page_to_load(driver)

        upload_btn = driver.find_element(By.ID, "upload_button")
        upload_btn.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)
        time.sleep(2)  # Force wait time

        assert driver.current_url == f"{host}/dataset/list", "Test failed!"

        driver.get(f"{host}/community/Super%20Important%20Community/")

        link = driver.find_element(By.LINK_TEXT, "Title")
        link.click()
        time.sleep(3)
        wait_for_page_to_load(driver)
        print("Test passed!")

    finally:

        # Close the browser
        close_driver(driver)


# Call the test functions
test_join_community()

test_create_community()

test_upload_dataset_to_community()
