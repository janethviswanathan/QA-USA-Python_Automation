from selenium.webdriver.common.by import By
from selenium import webdriver
import time

def test_custom_scooter():
    # Create a driver for Chrome
    driver = webdriver.Chrome()

    # Go to the URL - update URL after starting server
    driver.get('https://cnt-89ef60d2-1a02-4998-870a-df13fc491fba.containerhub.tripleten-services.com/')

    # Enter From
    driver.find_element(By.ID, 'from').send_keys('East 2nd Street, 601')

    # Enter To
    driver.find_element(By.ID, 'to').send_keys('1300 1st St')

    # Click Custom
    driver.find_element(By.XPATH, '//div[text()="Custom"]').click()
    time.sleep(2)

    # Click Scooter Icon
    driver.find_element(By.XPATH, '//img[@src="/static/media/scooter.cf9bb57e.svg"]').click()
    time.sleep(2)

    # Verify Scooter Text is exists
    actual_value = driver.find_element(By.XPATH, '//div[@class="results-text"]//div[@class="text"]').text
    expected_value = "Scooter"
    assert expected_value in actual_value, f"Expected {expected_value}, but got {actual_value}"

    time.sleep(2)
    # Close the driver
    driver.quit()
