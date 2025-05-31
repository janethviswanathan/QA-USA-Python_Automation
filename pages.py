from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class UrbanRoutesPage:
    # ===============================
    # WebDriver Wait Timeout default 60
    # ===============================
    WEBDRIVER_WAIT_TIMEOUT = 60

    # ===============================
    # Address Input Locators
    # ===============================
    LOC_FROM_INPUT = (By.ID, "from")
    LOC_TO_INPUT = (By.ID, "to")

    # ===============================
    # Taxi Booking Locators
    # ===============================
    LOC_CALL_TAXI_BTN = (
        By.XPATH,
        "//button[contains(@class, 'button') and contains(@class, 'round')]",
    )

    # ===============================
    # Tariff Selection Locators
    # ===============================
    LOC_TARIFF_SUPPORTIVE = (
        By.XPATH,
        '//div[@class="tcard-icon"]/img[@alt="Supportive"]/ancestor::div[contains(@class, "tcard")]',
    )
    LOC_TARIFF_ACTIVE = (
        By.XPATH,
        '//div[contains(@class, "tcard active")]//div[contains(@class, "tcard-title")]',
    )

    # ===============================
    # Phone Verification Locators
    # ===============================
    LOC_PHONE_LABEL = (
        By.XPATH,
        '//div[@class="np-text" and text()="Phone number"]',
    )
    LOC_PHONE_INPUT = (By.ID, "phone")
    LOC_PHONE_NEXT_BTN = (By.XPATH, '//button[text()="Next"]')

    LOC_SMS_INPUT = (By.ID, "code")
    LOC_SMS_CONFIRM_BTN = (By.XPATH, '//button[text()="Confirm"]')

    # ===============================
    # Payment Method Locators
    # ===============================
    LOC_PAYMENT_BTN = (By.CLASS_NAME, "pp-button")
    LOC_PAYMENT_TEXT = (By.CLASS_NAME, "pp-value-text")
    LOC_PAYMENT_POPUP_CLOSE = (
        By.XPATH,
        '//div[contains(@class, "section") and contains(@class, "active") and .//div[text()="Payment method"]]//button[contains(@class, "section-close")]',
    )

    # ===============================
    # Card Modal Locators
    # ===============================
    LOC_CARD_ADD_BTN = (By.CLASS_NAME, "pp-plus")
    LOC_CARD_NUMBER_INPUT = (By.ID, "number")
    LOC_CARD_CODE_INPUT = (
        By.XPATH,
        '//div[@class="card-code-input"]/input[@name="code"]',
    )
    LOC_CARD_LINK_BTN = (By.XPATH, '//button[text()="Link"]')
    LOC_CARD_CHECKBOX = (
        By.XPATH,
        '//input[@type="checkbox" and @class="checkbox" and @name="card-1"]',
    )

    # ===============================
    # Additional Options Locators
    # ===============================
    LOC_COMMENT_INPUT = (By.ID, "comment")
    LOC_BLANKET_TOGGLE = (
        By.XPATH,
        '//div[@class="r-sw-container"][.//div[text()="Blanket and handkerchiefs"]]//span[@class="slider round"]',
    )
    LOC_BLANKET_CHECKBOX = (
        By.XPATH,
        '//div[contains(text(), "Blanket and handkerchiefs")]/ancestor::div[contains(@class, "r-sw-container")]//input',
    )
    LOC_ICE_CREAM_PLUS = (
        By.XPATH,
        '//div[@class="r-counter-container"][.//div[text()="Ice cream"]]//div[@class="counter-plus"]',
    )
    LOC_ICE_CREAM_COUNT = (
        By.XPATH,
        '//div[@class="r-counter-container"][.//div[text()="Ice cream"]]//div[@class="counter-value"]',
    )

    # ===============================
    # Order and Confirmation Locators
    # ===============================
    LOC_ORDER_BTN = (
        By.XPATH,
        '//button[@class="smart-button" and .//span[text()="Order"]]',
    )
    LOC_ORDER_BODY = (By.CSS_SELECTOR, "div.order")
    LOC_ORDER_HEADER_TIME = (By.CLASS_NAME, "order-header-time")
    LOC_ORDER_HEADER = (
        By.XPATH,
        '//div[@class="order-header-title" and contains(text(), "The driver will arrive in")]',
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WEBDRIVER_WAIT_TIMEOUT)

    # Address Input Methods
    def set_address_from(self, value):
        return self.__send_keys_to_element(self.LOC_FROM_INPUT, value)

    def set_address_to(self, value):
        self.__send_keys_to_element(self.LOC_TO_INPUT, value)

    def get_address_from(self):
        return self.__get_element_value_attribute(self.LOC_FROM_INPUT)

    def get_address_to(self):
        return self.__get_element_value_attribute(self.LOC_TO_INPUT)

    def click_call_taxi(self):
        self.__button_click(self.LOC_CALL_TAXI_BTN)

    # Tariff Actions
    def choose_supportive_tariff(self):
        self.__button_click(self.LOC_TARIFF_SUPPORTIVE)

    def get_active_tariff_name(self):
        return self.__get_locator_text(self.LOC_TARIFF_ACTIVE)

    # Phone Verification
    def click_phone_label(self):
        self.__button_click(self.LOC_PHONE_LABEL)

    def enter_phone_number(self, phone):
        self.__send_keys_to_element(self.LOC_PHONE_INPUT, phone)

    def click_next_on_phone(self):
        self.__button_click(self.LOC_PHONE_NEXT_BTN)

    def enter_sms_code(self, code):
        self.__send_keys_to_element(self.LOC_SMS_INPUT, code)

    def confirm_sms_code(self):
        self.__button_click(self.LOC_SMS_CONFIRM_BTN)

    def get_entered_phone(self):
        return self.__get_element_value_attribute(self.LOC_PHONE_INPUT)

    # Payment
    def open_payment_methods(self):
        self.__button_click(self.LOC_PAYMENT_BTN)

    def get_payment_text(self):
        return self.__get_locator_text(self.LOC_PAYMENT_TEXT)

    def close_payment_popup(self):
        self.__button_click(self.LOC_PAYMENT_POPUP_CLOSE)

    # Card Form
    def click_add_card(self):
        self.__button_click(self.LOC_CARD_ADD_BTN)

    def enter_card_number(self, number):
        self.__send_keys_to_element(self.LOC_CARD_NUMBER_INPUT, number)

    def enter_card_code(self, code):
        self.__send_keys_to_element(self.LOC_CARD_CODE_INPUT, code)

    def tab_from_card_code(self):
        self.__send_keys_to_element(self.LOC_CARD_CODE_INPUT, Keys.TAB)

    def click_link_card(self):
        self.__button_click(self.LOC_CARD_LINK_BTN)

    def is_card_checkbox_selected(self):
        return self.__check_element_selected(self.LOC_CARD_CHECKBOX)

    # Ride Options
    def enter_driver_note(self, message):
        self.__send_keys_to_element(self.LOC_COMMENT_INPUT, message)

    def get_driver_note(self):
        return self.__get_element_value_attribute(self.LOC_COMMENT_INPUT)

    def toggle_blanket(self):
        self.__button_scroll_click(self.LOC_BLANKET_TOGGLE)

    def is_blanket_toggled(self):
        return self.__check_element_selected(self.LOC_BLANKET_CHECKBOX)

    def add_ice_cream(self):
        self.__button_scroll_click(self.LOC_ICE_CREAM_PLUS)

    def get_ice_cream_count(self):
        return self.__get_locator_text(self.LOC_ICE_CREAM_COUNT)

    # Final Order
    def submit_order(self):
        self.__button_scroll_click(self.LOC_ORDER_BTN)

    def get_order_state_class(self):
        return self.__get_element_class_attribute(self.LOC_ORDER_BODY)

    def get_eta_text(self):
        return self.__get_locator_text(self.LOC_ORDER_HEADER)

    def __send_keys_to_element(self, locator, keys):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(keys)

    def __button_click(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        button.click()

    def __button_scroll_click(self, locator):
        button = self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", button
        )
        self.driver.execute_script("arguments[0].click();", button)

    def __get_element_value_attribute(self, locator):
        print(locator)
        return self.wait.until(
            EC.presence_of_element_located(locator)
        ).get_attribute("value")

    def __get_element_class_attribute(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        ).get_attribute("class")

    def __get_locator_text(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).text

    def __check_element_selected(self, locator):
        return self.wait.until(
            EC.presence_of_element_located(locator)
        ).is_selected()
