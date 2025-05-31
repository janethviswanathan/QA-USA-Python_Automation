from selenium.webdriver.common.by import By

class UrbanRoutesPage:
    # Locators as class attributes
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CUSTOM_OPTION_LOCATOR = (By.XPATH, '//div[text()="Custom"]')
    SCOOTER_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]')
    SCOOTER_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')
    BIKE_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/bike.b0d16d8b.svg"]')
    BIKE_TEXT_LOCATOR = (By.XPATH, '//div[@class="results-text"]//div[@class="text"]')

    def __init__(self, driver):
        self.driver = driver

    def enter_from_location(self, from_text):
        # Enter From
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)

    def enter_to_location(self, to_text):
        # Enter To
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from_location_text(self):
        # Return the "from location" input field value
        return self.driver.find_element(*self.FROM_LOCATOR).text

    def get_to_location_text(self):
        # Return the "to location" input field value
        return self.driver.find_element(*self.TO_LOCATOR).text

    def click_custom_option(self):
        # Click Custom
        self.driver.find_element(*self.CUSTOM_OPTION_LOCATOR).click()

    def click_scooter_icon(self):
        # Click Scooter Icon
        self.driver.find_element(*self.SCOOTER_ICON_LOCATOR).click()

    def get_scooter_text(self):
        # Return the "Scooter" text
        return self.driver.find_element(*self.SCOOTER_TEXT_LOCATOR).text

    def click_bike_icon(self):
        # Click Bike Icon
        print(self.driver.find_elements(*self.BIKE_ICON_LOCATOR))
        self.driver.find_element(*self.BIKE_ICON_LOCATOR).click()

    def get_bike_text(self):
        # Return the "Bike" text
        return self.driver.find_element(*self.BIKE_TEXT_LOCATOR).text