# main.py
import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities

        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {"performance": "ALL"}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(5)
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print(
                "Cannot connect to Urban Routes. Check the server is on and still running"
            )

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        actual_from_address, actual_to_address = page.get_route()
        assert actual_from_address == data.ADDRESS_FROM, (
            f"Expected '{data.ADDRESS_FROM}', got '{actual_from_address}'"
        )
        assert actual_to_address == data.ADDRESS_TO, (
            f"Expected '{data.ADDRESS_TO}', got '{actual_to_address}'"
        )

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.choose_supportive_tariff()
        active_tariff = page.get_active_tariff_name()
        assert active_tariff == "Supportive", (
            f"Expected active tariff 'Supportive', got '{active_tariff}'"
        )

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.choose_supportive_tariff()
        page.click_phone_label()
        page.enter_phone_number(data.PHONE_NUMBER)
        page.click_next_on_phone()
        code = helpers.retrieve_phone_code(self.driver)
        page.enter_sms_code(code)
        page.confirm_sms_code()
        assert page.get_entered_phone() == data.PHONE_NUMBER, (
            f"Expected phone number '{data.PHONE_NUMBER}', got '{page.get_entered_phone()}'"
        )

    def test_payment_method_entered(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.choose_supportive_tariff()
        page.open_payment_methods()
        page.click_add_card()
        page.enter_card_number(data.CARD_NUMBER)
        page.enter_card_code(data.CARD_CODE)
        page.tab_from_card_code()
        page.click_link_card()
        page.close_payment_popup()
        assert page.get_payment_text() == "Card", (
            f"Expected payment method 'Card', got '{page.get_payment_text()}'"
        )

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.choose_supportive_tariff()
        page.enter_driver_note(data.MESSAGE_FOR_DRIVER)
        assert page.get_driver_note() == data.MESSAGE_FOR_DRIVER, (
            f"Expected driver message '{data.MESSAGE_FOR_DRIVER}', got '{page.get_driver_note()}'"
        )

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.choose_supportive_tariff()
        if not page.is_blanket_toggled():
            page.toggle_blanket()
        assert page.is_blanket_toggled(), (
            f"Expected blanket option to be selected, got '{page.is_blanket_toggled()}'"
        )

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.choose_supportive_tariff()
        for _ in range(2):  # Increase ice cream count by 2
            page.add_ice_cream()
        assert page.get_ice_cream_count() == "2", (
            f"Expected ice cream value to be 2, got '{page.get_ice_cream_count()}'"
        )

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.choose_supportive_tariff()
        page.submit_order()
        assert page.get_order_state_class() == "order shown", (
            f"Expected Order Popup Menu visible to be 'True', but got '{page.get_order_state_class()}'"
        )

    def test_order_eta_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        page.click_call_taxi()
        page.choose_supportive_tariff()
        eta_text = page.get_eta_text()
        assert "The driver will arrive in" in eta_text, (
            f"Expected 'The driver will arrive in' in order-header-title, but {eta_text} was found"
        )

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
