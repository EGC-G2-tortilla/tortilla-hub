import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


SAMPLE_DATASET_ROUTE = "/doi/10.1234/dataset2/"  # Route for Sample Dataset 1


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


# WI: Dashboard
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


# WI: Staging area
def test_stage_dataset():
    driver = initialize_driver()
    driver.maximize_window()

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
            By.ID,
            "unstaged-datasets",
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
            By.ID,
            "unstaged-datasets",
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
    driver.maximize_window()

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
            By.ID,
            "staged-datasets",
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
        staged_table = driver.find_element(By.ID, "staged-datasets")
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
    driver.maximize_window()

    try:
        host = "http://localhost:5000"

        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        driver.find_element(By.NAME, "email").send_keys("user1@example.com")
        driver.find_element(By.NAME, "password").send_keys("1234", Keys.RETURN)
        wait_for_page_to_load(driver)

        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Find "Stage All" button
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        stage_all_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "stage-all-button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", stage_all_button)

        stage_all_button.click()

        # Wait for all unstaged rows to disappear
        WebDriverWait(driver, 10).until(
            lambda d: len(
                driver.find_elements(By.CSS_SELECTOR, "#unstaged-datasets tbody tr")
            )
            == 0
        )
        wait_for_page_to_load(driver)

        print("All datasets staged successfully.")

    finally:
        close_driver(driver)


def test_unstage_all_datasets():
    driver = initialize_driver()
    driver.maximize_window()

    try:
        host = "http://localhost:5000"

        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        driver.find_element(By.NAME, "email").send_keys("user1@example.com")
        driver.find_element(By.NAME, "password").send_keys("1234", Keys.RETURN)
        wait_for_page_to_load(driver)

        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Locate and click the "Unstage all datasets" button
        unstage_all_button = driver.find_element(By.ID, "unstage-all-button")
        driver.execute_script("arguments[0].scrollIntoView(true);", unstage_all_button)
        unstage_all_button.click()

        # Wait for the table to update
        WebDriverWait(driver, 10).until(
            lambda d: len(
                driver.find_elements(By.CSS_SELECTOR, "#staged-datasets tbody tr")
            )
            == 0
        )
        wait_for_page_to_load(driver)

        print("All datasets unstaged successfully.")

    finally:
        close_driver(driver)


def test_publish_datasets():
    driver = initialize_driver()
    driver.maximize_window()

    try:
        host = "http://localhost:5000"

        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        # Login
        driver.find_element(By.NAME, "email").send_keys("user1@example.com")
        driver.find_element(By.NAME, "password").send_keys("1234", Keys.RETURN)
        wait_for_page_to_load(driver)

        driver.get(f"{host}/dataset/list")
        wait_for_page_to_load(driver)

        # Find "Publish All" button
        publish_all_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "publish-all-button"))
        )
        driver.execute_script("arguments[0].scrollIntoView(true);", publish_all_button)
        publish_all_button.click()

        # Wait for all staged datasets to disappear
        WebDriverWait(driver, 10).until(
            lambda d: len(
                driver.find_elements(By.CSS_SELECTOR, "#staged-datasets tbody tr")
            )
            == 0
        )
        wait_for_page_to_load(driver)

        print("All datasets published successfully.")

    finally:
        close_driver(driver)


# WI: Improve UI
def test_buttons_upload_and_download():
    """Test to verify the presence and layout of buttons on the page."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}/login")
        wait_for_page_to_load(driver)

        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        password_input = driver.find_element(By.NAME, "password")
        username_input.send_keys("user2@example.com")
        password_input.send_keys("1234")
        password_input.send_keys(Keys.RETURN)
        wait_for_page_to_load(driver)

        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Verify the "Download all" button
        download_button = driver.find_element(By.ID, "download-all-button")
        assert download_button.is_displayed(), "Download all button is not displayed!"

        # Verify "Upload from Github" button
        github_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "repoUrlInput"))
        )
        assert (
            github_button.is_displayed()
        ), "Upload from Github button is not displayed!"

        # Verify the "Upload from ZIP" button
        zip_button = driver.find_element(By.ID, "uploadButton")
        assert zip_button.is_displayed(), "Upload from ZIP button is not displayed!"

        print("Button layout test passed!")

    finally:
        close_driver(driver)


def test_file_table():
    """Test to verify that files are displayed correctly in the table."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the dataset view page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Verify the table rows
        rows = driver.find_elements(
            By.XPATH, "//div[@class='list-group-item file-item']"
        )
        assert len(rows) > 0, "No files are displayed in the table!"

        for row in rows:
            # Verify file name
            file_name = row.find_element(By.XPATH, ".//div[contains(@class, 'col-8')]")
            assert file_name.is_displayed(), "File name is not displayed!"

            # Verify "View" button
            view_button = row.find_element(By.XPATH, ".//button[contains(., 'View')]")
            assert view_button.is_displayed(), "View button is not displayed!"

            # Verify "Check" button
            check_button = row.find_element(By.XPATH, ".//button[contains(., 'Check')]")
            assert check_button.is_displayed(), "Check button is not displayed!"

            # Verify "Export" button
            export_button = row.find_element(
                By.XPATH, ".//button[contains(., 'Export')]"
            )
            assert export_button.is_displayed(), "Export button is not displayed!"

        print("File table test passed!")

    finally:
        close_driver(driver)


def test_metadata_display():
    """Test to verify that metadata (title, description, authors, etc.) is displayed correctly."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the dataset view page
        driver.get(
            f"{host}{SAMPLE_DATASET_ROUTE}"
        )  # Ensure that this dataset exists and has correct data
        wait_for_page_to_load(driver)

        # Verify the title
        title = driver.find_element(By.TAG_NAME, "h1")
        assert title.is_displayed(), "Dataset title is not displayed!"

        # Locate the 'About' section
        about_section = driver.find_element(By.XPATH, "//span[contains(., 'About')]")
        assert about_section.is_displayed(), "'About' heading is not displayed!"

        # Find the <p> element containing the description
        description = about_section.find_element(
            By.XPATH, "./ancestor::div[contains(@class, 'row')]//p[@class='card-text']"
        )
        assert description.is_displayed(), "Dataset description is not displayed!"

        # Locate the authors section
        authors_section = driver.find_element(
            By.XPATH, "//span[contains(., 'Authors')]"
        )
        assert authors_section.is_displayed(), "'Authors' heading is not displayed!"

        # Find the <p> elements containing the authors' names
        authors = authors_section.find_elements(
            By.XPATH, "./ancestor::div[contains(@class, 'row')]//p"
        )
        assert len(authors) > 0, "Authors are not displayed!"

        # Verify the publication DOI
        try:
            doi_section = driver.find_element(
                By.XPATH, "//span[contains(., 'Publication DOI')]"
            )
            assert (
                doi_section.is_displayed()
            ), "'Publication DOI' heading is not displayed!"

            doi = doi_section.find_element(
                By.XPATH, "./ancestor::div[contains(@class, 'row')]//p"
            )
            assert doi.is_displayed(), "Publication DOI is not displayed!"

            print("Publication DOI is displayed.")
        except NoSuchElementException:
            print("Publication DOI is not available for this dataset.")

        print("Metadata display test passed!")

    finally:
        close_driver(driver)


def test_interactive_elements():
    """Test to verify interactive elements like buttons and dropdowns work."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the dataset view page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Click on the "View" button for the first file
        view_button = driver.find_element(
            By.XPATH, "(//button[contains(., 'View')])[1]"
        )
        view_button.click()
        time.sleep(1)  # Wait for modal to appear

        # Verify the modal
        modal = driver.find_element(By.ID, "fileViewerModal")
        assert modal.is_displayed(), "File viewer modal is not displayed!"

        # Close the modal
        close_button = modal.find_element(By.CLASS_NAME, "btn-close")
        close_button.click()
        time.sleep(1)  # Wait for modal to disappear
        assert not modal.is_displayed(), "File viewer modal did not close!"

        print("Interactive elements test passed!")

    finally:
        close_driver(driver)


def test_file_search_functionality():
    """Test the 'Go to file...' search functionality."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Ensure there are files to search
        files = driver.find_elements(By.CSS_SELECTOR, ".file-item")
        assert len(files) > 1, "Not enough files to test search functionality!"

        # Get the name of a file to search for
        file_to_search = files[0].get_attribute("data-file-name")

        # Type the file name into the search input
        search_input = driver.find_element(By.ID, "fileSearch")
        search_input.clear()
        search_input.send_keys(file_to_search)
        time.sleep(1)  # Wait for the filtering to take effect

        # Verify that only the matching file is displayed
        visible_files = [file for file in files if file.is_displayed()]
        assert len(visible_files) == 1, "Search did not filter files correctly!"
        assert (
            visible_files[0].get_attribute("data-file-name") == file_to_search
        ), "Displayed file does not match search query!"

        # Clear the search input
        search_input.clear()
        search_input.send_keys(Keys.BACKSPACE)
        time.sleep(1)

        # Verify that all files are displayed again
        all_files_visible = all(file.is_displayed() for file in files)
        assert all_files_visible, "Not all files are displayed after clearing search!"

        print("File search functionality test passed!")

    finally:
        close_driver(driver)


def test_explore_more_datasets():
    """Test the 'Explore more datasets' button functionality."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Locate the 'Explore more datasets' button
        explore_button = driver.find_element(
            By.XPATH, "//a[contains(., 'Explore more datasets')]"
        )
        assert (
            explore_button.is_displayed()
        ), "'Explore more datasets' button is not displayed!"

        # Click the button
        explore_button.click()
        wait_for_page_to_load(driver)

        # Verify that the URL has changed to the expected page
        expected_url = f"{host}/explore"
        current_url = driver.current_url
        assert (
            current_url == expected_url
        ), f"Did not navigate to the explore page! Current URL: {current_url}"

        print("Explore more datasets test passed!")

    finally:
        close_driver(driver)


def test_check_button_functionality():
    """Test the 'Check' button functionality."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Find the first file item
        file_items = driver.find_elements(By.CSS_SELECTOR, ".file-item")
        assert len(file_items) > 0, "No file items found!"

        first_file_item = file_items[0]

        # Get the file ID from the 'check_<file.id>' div
        output_div = first_file_item.find_element(
            By.XPATH, ".//div[starts-with(@id, 'check_')]"
        )
        output_div_id = output_div.get_attribute("id")
        file_id = output_div_id.replace("check_", "")

        # Click on the 'Check' button to expand the dropdown
        check_button = first_file_item.find_element(
            By.XPATH, f".//button[@id='btnGroupDrop{file_id}']"
        )
        check_button.click()
        time.sleep(1)  # Wait for dropdown to expand

        # Click on the 'Syntax check' option
        syntax_check_option = first_file_item.find_element(
            By.XPATH,
            f".//ul[@aria-labelledby='btnGroupDrop{file_id}'] \
            //a[contains(., 'Syntax check')]",
        )
        syntax_check_option.click()
        # Wait for the result to appear in the output div
        output_div = driver.find_element(By.ID, f"check_{file_id}")
        WebDriverWait(driver, 10).until(lambda d: output_div.text.strip() != "")

        # Verify the result
        result_text = output_div.text.strip()
        assert (
            "Valid Model" in result_text
            or "Errors" in result_text
            or "Error" in result_text
        ), f"Unexpected result text: {result_text}"

        print("Check button functionality test passed!")

    finally:
        close_driver(driver)


# Call the test function

# WI: Dashboard
test_data_display()

# WI: Staging area
test_stage_dataset()
test_unstage_dataset()
test_stage_all_datasets()
test_unstage_all_datasets()
test_stage_all_datasets()
test_publish_datasets()

# WI: Improve UI
test_buttons_upload_and_download()
test_file_table()
test_metadata_display()
test_interactive_elements()
test_file_search_functionality()
test_explore_more_datasets()
test_check_button_functionality()
