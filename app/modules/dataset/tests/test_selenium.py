import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import initialize_driver, close_driver


SAMPLE_DATASET_ROUTE = "/doi/10.1234/dataset1/"  # Route for Sample Dataset 1


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


def test_buttons_upload_and_download():
    """Test to verify the presence and layout of buttons on the page."""
    driver = initialize_driver()

    try:
        host = get_host_for_selenium_testing()

        # Open the dataset view page
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")
        wait_for_page_to_load(driver)

        # Verify the "Download all" button
        download_button = driver.find_element(By.XPATH, "//a[contains(., 'Download all')]")
        assert download_button.is_displayed(), "Download all button is not displayed!"

        # Verify the "Upload from Github" button
        github_button = driver.find_element(By.XPATH, "//a[contains(., 'Upload from Github')]")
        assert github_button.is_displayed(), "Upload from Github button is not displayed!"

        # Verify the "Upload from ZIP" button
        zip_button = driver.find_element(By.XPATH, "//a[contains(., 'Upload from ZIP')]")
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
        rows = driver.find_elements(By.XPATH, "//div[@class='list-group-item file-item']")
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
            export_button = row.find_element(By.XPATH, ".//button[contains(., 'Export')]")
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
        driver.get(f"{host}{SAMPLE_DATASET_ROUTE}")  # Ensure that this dataset exists and has correct data
        wait_for_page_to_load(driver)

        # Verify the title
        title = driver.find_element(By.TAG_NAME, "h1")
        assert title.is_displayed(), "Dataset title is not displayed!"

        # Locate the 'About' section
        about_section = driver.find_element(By.XPATH, "//span[contains(., 'About')]")
        assert about_section.is_displayed(), "'About' heading is not displayed!"

        # Find the <p> element containing the description
        description = about_section.find_element(
            By.XPATH,
            "./ancestor::div[contains(@class, 'row')]//p[@class='card-text']"
        )
        assert description.is_displayed(), "Dataset description is not displayed!"

        # Locate the authors section
        authors_section = driver.find_element(By.XPATH, "//span[contains(., 'Authors')]")
        assert authors_section.is_displayed(), "'Authors' heading is not displayed!"

        # Find the <p> elements containing the authors' names
        authors = authors_section.find_elements(
            By.XPATH,
            "./ancestor::div[contains(@class, 'row')]//p"
        )
        assert len(authors) > 0, "Authors are not displayed!"

        # Verify the publication DOI
        try:
            doi_section = driver.find_element(By.XPATH, "//span[contains(., 'Publication DOI')]")
            assert doi_section.is_displayed(), "'Publication DOI' heading is not displayed!"

            doi = doi_section.find_element(
                By.XPATH,
                "./ancestor::div[contains(@class, 'row')]//p"
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
        view_button = driver.find_element(By.XPATH, "(//button[contains(., 'View')])[1]")
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
        assert visible_files[0].get_attribute("data-file-name") == file_to_search, \
            "Displayed file does not match search query!"

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
        explore_button = driver.find_element(By.XPATH, "//a[contains(., 'Explore more datasets')]")
        assert explore_button.is_displayed(), "'Explore more datasets' button is not displayed!"

        # Click the button
        explore_button.click()
        wait_for_page_to_load(driver)

        # Verify that the URL has changed to the expected page
        expected_url = f"{host}/explore"
        current_url = driver.current_url
        assert current_url == expected_url, f"Did not navigate to the explore page! Current URL: {current_url}"

        print("Explore more datasets test passed!")

    finally:
        close_driver(driver)
# Call the test functions
# test_upload_dataset()


test_data_display()


test_buttons_upload_and_download()


test_file_table()


test_metadata_display()


test_interactive_elements()


test_file_search_functionality()


test_explore_more_datasets()
