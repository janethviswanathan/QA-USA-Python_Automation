import time
from selenium import webdriver
from orig_pages import UrbanRoutesPage  # Import the POM class
from data import *
from selenium.webdriver.common.by import By

def test_custom_bike_option():
    # Open the app - update the URL after starting the server
    driver = webdriver.Chrome()
    driver.get('https://cnt-41afad9c-ac54-4750-8eed-9261a917f508.containerhub.tripleten-services.com/')

    # Create an instance of the page class
    # urban_routes_page is the instance name that you created from UrbanRoutesPage
    urban_routes_page = UrbanRoutesPage(driver)

    urban_routes_page.enter_from_location(ADDRESS_FROM)
    urban_routes_page.enter_to_location(ADDRESS_TO)

    # Select the "Custom" option.
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the "Scooter" icon.
    print(driver.find_elements(by=By.NAME, value='bike_icon'))
    urban_routes_page.click_bike_icon()
    time.sleep(2)  # Adding delay for visibility; optional

    # # Verify the Scooter text is displayed correctly
    # actual_value = urban_routes_page.get_bike_text()
    # expected_value = "Bike"
    # assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"
    driver.quit()

test_custom_bike_option()