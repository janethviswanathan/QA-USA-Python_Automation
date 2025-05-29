# main.py

from selenium.webdriver.common.by import By
from data import *
from helpers import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

# driver.implicitly_wait(3)
# driver.find_element(By.TAG_NAME, "button")
# driver.find_element(By.TAG_NAME, "div")
# driver.find_element(By.TAG_NAME, "button")
# driver.find_element(By.TAG_NAME, "imput")
# driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")
# driver.find_element(By.ID, "to").send_keys("1300 1st St")
# driver.find_element(By.ID, "from").clear()
# driver.find_element(By.CLASS_NAME, "logo-disclaimer").text

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
      if is_url_reachable(URBAN_ROUTES_URL):
          print("Connected to the Urban Routes server")
      else:
          print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        # Add in S8
        print("function created for set route")
        pass

    def test_select_plan(self):
        # Add in S8
        print("function created for select plan")
        pass

    def test_fill_phone_number(self):
        # Add in S8
        print("function created for fill phone number")
        pass

    def test_fill_card(self):
        # Add in S8
        print("function created for fill card")
        pass

    def test_comment_for_driver(self):
        # Add in S8
        print("function created for comment for driver")
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Add in S8
        print("function created for order blanket and handkerchiefs")
        pass

    def test_order_2_ice_creams(self):
        # Add in S8
        print("function created for order 2 ice creams")
        for _ in range(2):
            # Add in S8
            pass

    def test_car_search_model_appears(self):
        # Add in S8
        print("function created for car search model appears")
        pass