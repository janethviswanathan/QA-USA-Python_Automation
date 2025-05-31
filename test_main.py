# main.py
from data import *
from helpers import *
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    driver = webdriver.Chrome()

    @classmethod
    def setup_class(cls):
      if is_url_reachable(URBAN_ROUTES_URL):
          # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
          from selenium.webdriver import DesiredCapabilities
          capabilities = DesiredCapabilities.CHROME
          capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
          cls.driver = webdriver.Chrome()
          cls.driver.get(URBAN_ROUTES_URL)
      else:
          assert is_url_reachable(URBAN_ROUTES_URL), "Urban Routes URL is unreachable"

    def test_set_route(self):
        # Fill From and To input fields for route
        page = UrbanRoutesPage(self.driver)
        page.set_address_from(ADDRESS_FROM)
        page.set_address_to(ADDRESS_TO)

        # Retrieve values of From and To fields
        from_address_value = page.get_address_from()
        to_address_value = page.get_address_to()

        # Test that values were set
        assert from_address_value == ADDRESS_FROM, f"Expected '{ADDRESS_FROM}', got '{from_address_value}'"
        assert to_address_value == ADDRESS_TO, f"Expected '{ADDRESS_TO}', got '{to_address_value}'"

    def test_select_plan(self):
        page = UrbanRoutesPage(self.driver)
        # if not page.get_taxi_active_icon():
        #     page.select_taxi_icon()
        page.select_call_taxi_icon()
        active_tariff = page.get_active_tariff()
        print(f"The active tariff is '{active_tariff}'")
        if active_tariff != 'Supportive':
            page.select_supportive_tariff()
        assert page.get_active_tariff() == 'Supportive'

    #
    # def test_fill_phone_number(self):
    #     page = UrbanRoutesPage(self.driver)
    #     page.enter_phone_number(PHONE_NUMBER)
    #     page.click_next_after_phone()
    #     code = retrieve_phone_code(self.driver)
    #     page.enter_sms_code(code)
    #     page.confirm_sms_code()
    #     assert True
    #
    # def test_fill_card(self):
    #     page = UrbanRoutesPage(self.driver)
    #     page.click_payment_method()
    #     page.click_add_card_plus()
    #     page.fill_card_number(CARD_NUMBER)
    #     page.fill_card_code(CARD_CODE)
    #     page.link_card()
    #     assert True
    #
    # def test_comment_for_driver(self):
    #     page = UrbanRoutesPage(self.driver)
    #     page.enter_driver_message(MESSAGE_FOR_DRIVER)
    #     assert True
    #
    # def test_order_blanket_and_handkerchiefs(self):
    #     page = UrbanRoutesPage(self.driver)
    #     if not page.is_blanket_selected():
    #         page.toggle_blanket_option()
    #     assert page.is_blanket_selected() is True
    #
    # def test_order_2_ice_creams(self):
    #     page = UrbanRoutesPage(self.driver)
    #     for _ in range(2):
    #         page.increase_ice_cream()
    #     assert page.get_ice_cream_value() == '3'  # Includes 1 default + 2 = 3
    #
    # def test_car_search_model_appears(self):
    #     page = UrbanRoutesPage(self.driver)
    #     page.click_order_button()
    #     assert "Taxi" in page.get_search_modal_text()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()