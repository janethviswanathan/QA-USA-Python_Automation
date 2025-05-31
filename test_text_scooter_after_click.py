import time
from selenium import webdriver
from pages import UrbanRoutesPage  # Import the POM class
from data import *

def test_custom_scooter_option():
    # Open the app - update the URL after starting the server
    from selenium.webdriver import DesiredCapabilities
    capabilities = DesiredCapabilities.CHROME
    capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
    driver = webdriver.Chrome()
    driver.get(URBAN_ROUTES_URL)

    # Create an instance of the page class
    # urban_routes_page is the instance name that you created from UrbanRoutesPage
    urban_routes_page = UrbanRoutesPage(driver)

    urban_routes_page.set_address_from(ADDRESS_FROM)
    urban_routes_page.set_address_to(ADDRESS_TO)

    # Select the "Custom" option.
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the "Scooter" icon.
    urban_routes_page.click_scooter_icon()
    time.sleep(2)  # Adding delay for visibility; optional

    # Verify the Scooter text is displayed correctly
    actual_value = urban_routes_page.get_scooter_text()
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
    driver.quit()
