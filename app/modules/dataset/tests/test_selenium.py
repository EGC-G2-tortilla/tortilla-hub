from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


def wait_for_page_to_load(driver, timeout=4):
    WebDriverWait(driver, timeout).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )


def count_datasets(driver, host):
    driver.get(f"{host}/dataset/list")
    wait_for_page_to_load(driver)

    try:
        amount_datasets = len(driver.find_elements(By.XPATH, "//table//tbody//tr"))
    except Exception:
        amount_datasets = 0
    return amount_datasets


# def test_upload_dataset():
#     driver = initialize_driver()

#     try:
#         host = get_host_for_selenium_testing()

#         # Open the login page
#         driver.get(f"{host}/login")
#         wait_for_page_to_load(driver)

#         # Find the username and password field and enter the values
#         email_field = driver.find_element(By.NAME, "email")
#         password_field = driver.find_element(By.NAME, "password")

#         email_field.send_keys("user1@example.com")
#         password_field.send_keys("1234")

#         # Send the form
#         password_field.send_keys(Keys.RETURN)
#         wait_for_page_to_load(driver)

#         # Count initial datasets
#         initial_datasets = count_datasets(driver, host)

#         # Open the upload dataset
#         driver.get(f"{host}/dataset/upload")
#         wait_for_page_to_load(driver)

#         # Find basic info and UVL model and fill values
#         title_field = driver.find_element(By.NAME, "title")
#         title_field.send_keys("Title")
#         desc_field = driver.find_element(By.NAME, "desc")
#         desc_field.send_keys("Description")
#         tags_field = driver.find_element(By.NAME, "tags")
#         tags_field.send_keys("tag1,tag2")

#         # Add two authors and fill
#         add_author_button = driver.find_element(By.ID, "add_author")
#         add_author_button.send_keys(Keys.RETURN)
#         wait_for_page_to_load(driver)
#         add_author_button.send_keys(Keys.RETURN)
#         wait_for_page_to_load(driver)

#         name_field0 = driver.find_element(By.NAME, "authors-0-name")
#         name_field0.send_keys("Author0")
#         affiliation_field0 = driver.find_element(By.NAME, "authors-0-affiliation")
#         affiliation_field0.send_keys("Club0")
#         orcid_field0 = driver.find_element(By.NAME, "authors-0-orcid")
#         orcid_field0.send_keys("0000-0000-0000-0000")

#         name_field1 = driver.find_element(By.NAME, "authors-1-name")
#         name_field1.send_keys("Author1")
#         affiliation_field1 = driver.find_element(By.NAME, "authors-1-affiliation")
#         affiliation_field1.send_keys("Club1")

#         # Obtén las rutas absolutas de los archivos
#         file1_path = os.path.abspath("app/modules/dataset/uvl_examples/file1.uvl")
#         file2_path = os.path.abspath("app/modules/dataset/uvl_examples/file2.uvl")

#         # Subir el primer archivo
#         dropzone = driver.find_element(By.CLASS_NAME, "dz-hidden-input")
#         dropzone.send_keys(file1_path)
#         wait_for_page_to_load(driver)

#         # Subir el segundo archivo
#         dropzone = driver.find_element(By.CLASS_NAME, "dz-hidden-input")
#         dropzone.send_keys(file2_path)
#         wait_for_page_to_load(driver)

#         # Add authors in UVL models
#         show_button = driver.find_element(By.ID, "0_button")
#         show_button.send_keys(Keys.RETURN)
#         add_author_uvl_button = driver.find_element(By.ID, "0_form_authors_button")
#         add_author_uvl_button.send_keys(Keys.RETURN)
#         wait_for_page_to_load(driver)

#         name_field = driver.find_element(By.NAME, "feature_models-0-authors-2-name")
#         name_field.send_keys("Author3")
#         affiliation_field = driver.find_element(
#             By.NAME, "feature_models-0-authors-2-affiliation"
#         )
#         affiliation_field.send_keys("Club3")

#         # Check I agree and send form
#         check = driver.find_element(By.ID, "agreeCheckbox")
#         check.send_keys(Keys.SPACE)
#         wait_for_page_to_load(driver)

#         upload_btn = driver.find_element(By.ID, "upload_button")
#         upload_btn.send_keys(Keys.RETURN)
#         wait_for_page_to_load(driver)
#         time.sleep(2)  # Force wait time

#         assert driver.current_url == f"{host}/dataset/list", "Test failed!"

#         # Count final datasets
#         final_datasets = count_datasets(driver, host)
#         assert final_datasets == initial_datasets + 1, "Test failed!"

#         print("Test passed!")

#     finally:

#         # Close the browser
#         close_driver(driver)


def test_data_display():
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the main page
        driver.get(f"{host}/")
        wait_for_page_to_load(driver)

        # Check most popular datasets chart
        popular_datasets_chart = driver.find_element(By.ID, "popular-datasets-chart")
        assert (
            popular_datasets_chart.is_displayed()
        ), "Popular datasets chart not displayed!"

        # Check latest datasets
        latest_datasets_container = driver.find_element(
            By.ID, "latest-datasets-container"
        )
        assert (
            latest_datasets_container.is_displayed()
        ), "Latest datasets container not displayed!"

        # Check hub statistics
        hub_statistics_card = driver.find_element(By.ID, "hub-statistics-card")
        assert hub_statistics_card.is_displayed(), "Hub statistics card not displayed!"

        # Check most popular authors
        most_popular_authors_container = driver.find_element(
            By.ID, "most-popular-authors-container"
        )
        assert (
            most_popular_authors_container.is_displayed()
        ), "Most popular authors container not displayed!"

        print("Data display test passed!")

    finally:
        # Close the browser
        close_driver(driver)


def test_stage_dataset():
    driver = initialize_driver()

    try:
        # Dynamically get the host if applicable (adjust if unnecessary)
        host = "http://localhost:5000"

        # Navigate to the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Navigate to the datasets page
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Find the "Unstaged Datasets" table
        unstaged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Unstaged Datasets')]/following-sibling::table",
        )

        # Count the unstaged datasets
        unstaged_rows = unstaged_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_unstaged = len(unstaged_rows)

        # Verify that there is at least one unstaged dataset
        assert num_unstaged > 0, "There are no datasets to stage."

        # Find the stage button of the first unstaged dataset
        stage_button = unstaged_rows[0].find_element(
            By.CSS_SELECTOR, "form[action*='/dataset/stage/'] button"
        )
        stage_button.click()

        # Wait for the table to update
        WebDriverWait(driver, 5).until(
            EC.staleness_of(unstaged_rows[0])  # Wait for the first element to change
        )
        wait_for_page_to_load(driver)

        # Re-locate the table after the action
        unstaged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Unstaged Datasets')]/following-sibling::table",
        )
        unstaged_rows_after = unstaged_table.find_elements(By.CSS_SELECTOR, "tbody tr")

        # Verify that the dataset has been removed from the "Unstaged Datasets" table
        assert (
            len(unstaged_rows_after) == num_unstaged - 1
        ), "The dataset was not staged correctly."

        print("Dataset staged correctly.")

    finally:
        # Always close the browser
        close_driver(driver)


def test_unstage_dataset():
    driver = initialize_driver()

    try:
        # Dynamically get the host if applicable (adjust if unnecessary)
        host = "http://localhost:5000"

        # Navigate to the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Navigate to the datasets page
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Find the "Staged Datasets" table
        staged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Staged Datasets')]/following-sibling::table",
        )

        # Count the staged datasets
        staged_rows = staged_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_staged = len(staged_rows)

        # Verify that there is at least one staged dataset
        assert num_staged > 0, "There are no datasets to unstage."

        # Find the unstage button of the first staged dataset
        unstage_button = staged_rows[0].find_element(
            By.CSS_SELECTOR, "form[action*='/dataset/unstage/'] button"
        )
        unstage_button.click()

        # Wait for the table to update
        WebDriverWait(driver, 5).until(
            EC.staleness_of(staged_rows[0])  # Wait for the first element to change
        )
        wait_for_page_to_load(driver)

        # Re-locate the table after the action
        staged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Staged Datasets')]/following-sibling::table",
        )
        staged_rows_after = staged_table.find_elements(By.CSS_SELECTOR, "tbody tr")

        # Verify that the dataset has been removed from the "Staged Datasets" table
        assert (
            len(staged_rows_after) == num_staged - 1
        ), "The dataset was not unstaged correctly."

        print("Dataset unstaged correctly.")

    finally:
        # Always close the browser
        close_driver(driver)


def test_stage_all_datasets():
    driver = initialize_driver()

    try:
        # Dynamically get the host if applicable
        host = "http://localhost:5000"

        # Navigate to the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Navigate to the datasets page
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Verify that all datasets are in the "Unstaged" section
        unstaged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Unstaged Datasets')]/following-sibling::table",
        )
        unstaged_rows = unstaged_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_unstaged_before = len(unstaged_rows)
        assert (
            num_unstaged_before == 3
        ), f"Expected 3 unstaged datasets, but found {num_unstaged_before}."

        # Wait for the "Stage all datasets" form to be visible
        stage_all_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "form[action*='/dataset/stage/all']")
            )
        )

        # Locate the button within the form
        stage_all_button = stage_all_form.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        stage_all_button.click()

        # Wait for the page to reload or datasets to change state
        WebDriverWait(driver, 10).until(
            EC.staleness_of(unstaged_rows[0])
        )  # Wait for the first dataset to become stale
        wait_for_page_to_load(driver)

        # Verify that now all datasets are in the "Staged" section
        staged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Staged Datasets')]/following-sibling::table",
        )
        staged_rows = staged_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_staged_after = len(staged_rows)
        assert (
            num_staged_after == 3
        ), f"Expected 3 staged datasets, but found {num_staged_after}."

        print("All datasets have been staged correctly.")

    finally:
        # Always close the browser
        close_driver(driver)


def test_unstage_all_datasets():
    driver = initialize_driver()

    try:
        # Dynamically get the host if applicable
        host = "http://localhost:5000"

        # Navigate to the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Navigate to the datasets page
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Verify that all datasets are in the "Staged" section
        staged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Staged Datasets')]/following-sibling::table",
        )
        staged_rows = staged_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_staged_before = len(staged_rows)
        assert (
            num_staged_before == 3
        ), f"Expected 3 staged datasets, but found {num_staged_before}."

        # Wait for the "Unstage all datasets" form to be visible
        unstage_all_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "form[action*='/dataset/unstage/all']")
            )
        )

        # Locate the button within the form
        unstage_all_button = unstage_all_form.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        unstage_all_button.click()

        # Wait for the page to reload or datasets to change state
        WebDriverWait(driver, 10).until(
            EC.staleness_of(staged_rows[0])
        )  # Wait for the first dataset to become stale
        wait_for_page_to_load(driver)

        # Verify that now all datasets are back in the "Unstaged" section
        unstaged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Unstaged Datasets')]/following-sibling::table",
        )
        unstaged_rows = unstaged_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_unstaged_after = len(unstaged_rows)
        assert (
            num_unstaged_after == 3
        ), f"Expected 3 unstaged datasets, but found {num_unstaged_after}."

        print("All datasets have been unstaged correctly.")

    finally:
        # Always close the browser
        close_driver(driver)


def test_publish_datasets():
    driver = initialize_driver()

    try:
        # Dynamically get the host if applicable
        host = "http://localhost:5000"

        # Navigate to the login page
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        username_input = driver.find_element(By.NAME, "email")
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user1@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        # Navigate to the datasets page
        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Verify that all datasets are in the "Staged" section before publishing
        staged_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Staged Datasets')]/following-sibling::table",
        )
        staged_rows = staged_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_staged_before = len(staged_rows)
        assert (
            num_staged_before == 3
        ), f"Expected 3 staged datasets, but found {num_staged_before}."

        # Wait for the "Publish all datasets" form to be visible
        publish_all_form = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "form[action*='/dataset/publish']")
            )
        )

        # Locate the button within the form
        publish_all_button = publish_all_form.find_element(
            By.CSS_SELECTOR, "button[type='submit']"
        )
        publish_all_button.click()

        # Wait for the page to reload or datasets to change state
        WebDriverWait(driver, 10).until(
            EC.staleness_of(staged_rows[0])
        )  # Wait for the first dataset to become stale
        wait_for_page_to_load(driver)

        # Verify that all datasets are now in the "Published" section
        published_table = driver.find_element(
            By.XPATH,
            "//h5[contains(text(), 'Published Datasets')]/following-sibling::table",
        )
        published_rows = published_table.find_elements(By.CSS_SELECTOR, "tbody tr")
        num_published_after = len(published_rows)

        # Verify that the number of published datasets is equal to the number of staged datasets before publication
        assert (
            num_staged_before == num_published_after
        ), f"Expected {num_staged_before} published datasets, but found {num_published_after}."

        print("All datasets have been published correctly.")

    finally:
        # Always close the browser
        close_driver(driver)


# Call the test functions
# test_upload_dataset()
# test_data_display()
test_stage_dataset()
test_unstage_dataset()
test_stage_all_datasets()
test_unstage_all_datasets()
test_stage_all_datasets()
test_publish_datasets()
