# main.py
from data import (
    URBAN_ROUTES_URL,
    ADDRESS_FROM,
    ADDRESS_TO,
    PHONE_NUMBER,
    CARD_NUMBER,
    CARD_CODE,
    MESSAGE_FOR_DRIVER,
)
from helpers import is_url_reachable, retrieve_phone_code
from selenium import webdriver
from pages import UrbanRoutesPage
import time

PAGE_INTERACTION_WAIT_TIME = 1  # seconds


class TestUrbanRoutes:
    driver = webdriver.Chrome()

    @classmethod
    def setup_class(cls):
        # Check if url is reachable
        if is_url_reachable(URBAN_ROUTES_URL):
            # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
            from selenium.webdriver import DesiredCapabilities

            capabilities = DesiredCapabilities.CHROME
            capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
            cls.driver = webdriver.Chrome()
            cls.driver.get(URBAN_ROUTES_URL)
        else:
            assert is_url_reachable(URBAN_ROUTES_URL), (
                "Urban Routes URL is unreachable"
            )

    def test_set_from_address(self):
        page = UrbanRoutesPage(self.driver)
        page.set_address_from(ADDRESS_FROM)
        from_address_value = page.get_address_from()
        assert from_address_value == ADDRESS_FROM, (
            f"Expected '{ADDRESS_FROM}', got '{from_address_value}'"
        )

    def test_set_to_address(self):
        page = UrbanRoutesPage(self.driver)
        page.set_address_to(ADDRESS_TO)
        to_address_value = page.get_address_to()
        assert to_address_value == ADDRESS_TO, (
            f"Expected '{ADDRESS_TO}', got '{to_address_value}'"
        )

    def test_select_plan(self):
        page = UrbanRoutesPage(self.driver)
        page.click_call_taxi()
        active_tariff = page.get_active_tariff_name()
        if active_tariff != "Supportive":
            page.choose_supportive_tariff()
        active_tariff = page.get_active_tariff_name()
        assert active_tariff == "Supportive", (
            f"Expected active tariff 'Supportive', got '{active_tariff}'"
        )


    def test_fill_phone_number(self):
        page = UrbanRoutesPage(self.driver)
        page.click_phone_label()
        page.enter_phone_number(PHONE_NUMBER)
        page.click_next_on_phone()
        code = retrieve_phone_code(self.driver)
        page.enter_sms_code(code)
        page.confirm_sms_code()
        assert page.get_entered_phone() == PHONE_NUMBER, (
            f"Expected phone number '{PHONE_NUMBER}', got '{page.get_entered_phone()}'"
        )

    def test_fill_card(self):
        page = UrbanRoutesPage(self.driver)

        page.open_payment_methods()
        time.sleep(PAGE_INTERACTION_WAIT_TIME)  # Wait for page to load

        page.click_add_card()
        time.sleep(PAGE_INTERACTION_WAIT_TIME)  # Wait for page to load

        page.enter_card_number(CARD_NUMBER)
        time.sleep(PAGE_INTERACTION_WAIT_TIME)  # Wait for page to load

        page.enter_card_code(CARD_CODE)
        time.sleep(PAGE_INTERACTION_WAIT_TIME)  # Wait for page to load

        page.tab_from_card_code()
        time.sleep(PAGE_INTERACTION_WAIT_TIME)  # Wait for page to load

        page.click_link_card()
        assert page.is_card_checkbox_selected(), (
            f"Expected 'Card 1' selection is 'True', got '{page.is_card_checkbox_selected()}'"
        )

    def test_payment_method_entered(self):
        page = UrbanRoutesPage(self.driver)
        page.close_payment_popup()
        assert page.get_payment_text() == "Card", (
            f"Expected payment method 'Card', got '{page.get_payment_text()}'"
        )

    def test_comment_for_driver(self):
        page = UrbanRoutesPage(self.driver)
        page.enter_driver_note(MESSAGE_FOR_DRIVER)
        assert page.get_driver_note() == MESSAGE_FOR_DRIVER, (
            f"Expected driver message '{MESSAGE_FOR_DRIVER}', got '{page.get_driver_note()}'"
        )

    def test_order_blanket_and_handkerchiefs(self):
        page = UrbanRoutesPage(self.driver)
        if not page.is_blanket_toggled():
            page.toggle_blanket()
        assert page.is_blanket_toggled(), (
            f"Expected blanket option to be selected, got '{page.is_blanket_toggled()}'"
        )

    def test_order_2_ice_creams(self):
        page = UrbanRoutesPage(self.driver)
        for _ in range(2):  # Increase ice cream count by 2
            page.add_ice_cream()
        assert page.get_ice_cream_count() == "2", (
            f"Expected ice cream value to be 2, got '{page.get_ice_cream_count()}'"
        )

    def test_car_search_model_appears(self):
        page = UrbanRoutesPage(self.driver)
        page.submit_order()
        assert page.get_order_state_class() == "order shown", (
            f"Expected Order Popup Menu visible to be 'True', but got '{page.get_order_state_class()}'"
        )

    def test_order_eta_appears(self):
        page = UrbanRoutesPage(self.driver)
        eta_text = page.get_eta_text()
        assert "The driver will arrive in" in eta_text, (
            f"Expected 'The driver will arrive in' in order-header-title, but {eta_text} was found"
        )

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
