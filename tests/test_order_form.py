import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import MAIN_URL, ORDER_URL
from locators import MainPageLocators
from page_objects.order_page import OrderForm
from page_objects.rent_page import RentPage
from constants import TEST_ORDER_DATA  # Импортируем тестовые данные

@pytest.mark.usefixtures("setup")
class TestOrderForm:
    driver: webdriver.Firefox
    order_page: OrderForm
    rent_page: RentPage

    def test_setup(self):
        assert self.order_page is not None, "Order page object is not initialized"
        assert self.rent_page is not None, "Rent page object is not initialized"
        assert self.driver is not None, "Driver object is not initialized"
        print("Page and driver objects are initialized correctly")

    def navigate_to_order_page(self):
        print("Navigating to order page")
        order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.order_button)
        )
        order_button.click()

        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(ORDER_URL)
        )

    def test_fill_order_form(self):
        self.navigate_to_order_page()
        print(f"Filling out the order form with data: {TEST_ORDER_DATA[0]['name']}, {TEST_ORDER_DATA[0]['last_name']}, {TEST_ORDER_DATA[0]['address']}")
        self.order_page.set_name(TEST_ORDER_DATA[0]["name"])
        self.order_page.set_last_name(TEST_ORDER_DATA[0]["last_name"])
        self.order_page.set_address(TEST_ORDER_DATA[0]["address"])
        self.order_page.set_metro_station(TEST_ORDER_DATA[0]["metro_station"])
        self.order_page.set_telephone(TEST_ORDER_DATA[0]["telephone"])

        print("Checking the field values")
        self.order_page.check_name_value(TEST_ORDER_DATA[0]["name"])
        self.order_page.check_last_name_value(TEST_ORDER_DATA[0]["last_name"])
        self.order_page.check_address_value(TEST_ORDER_DATA[0]["address"])
        self.order_page.check_metro_station_value(TEST_ORDER_DATA[0]["metro_station"])
        self.order_page.check_telephone_value(TEST_ORDER_DATA[0]["telephone"])

        print("Clicking the next button")
        self.order_page.click_next_button()

        print("Navigating to rent page")
        self.rent_page.set_when_to_deliver_today()  # Выбор текущей даты
        self.rent_page.select_rental_period(TEST_ORDER_DATA[0]["rental_period"])  # Пример выбора срока аренды

        if TEST_ORDER_DATA[0]["color_option"] == "black":
            self.rent_page.select_black_color()
        elif TEST_ORDER_DATA[0]["color_option"] == "grey":
            self.rent_page.select_grey_color()
        self.rent_page.set_courier_comment(TEST_ORDER_DATA[0]["courier_comment"])
        self.rent_page.click_order_button()

        print("Confirming the order")
        self.rent_page.confirm_order()

    @pytest.mark.parametrize("order_data", TEST_ORDER_DATA[1:])  # Параметризируем тест с остальными данными
    def test_fill_order_form_with_new_data(self, order_data):
        print("Re-opening the browser")
        self.driver.get(MAIN_URL)

        self.navigate_to_order_page()
        print(f"Filling out the order form with new data: {order_data['name']}, {order_data['last_name']}, {order_data['address']}, {order_data['metro_station']}, {order_data['telephone']}")
        self.order_page.set_name(order_data["name"])
        self.order_page.set_last_name(order_data["last_name"])
        self.order_page.set_address(order_data["address"])
        self.order_page.set_metro_station(order_data["metro_station"])
        self.order_page.set_telephone(order_data["telephone"])

        print("Checking the field values")
        self.order_page.check_name_value(order_data["name"])
        self.order_page.check_last_name_value(order_data["last_name"])
        self.order_page.check_address_value(order_data["address"])
        self.order_page.check_metro_station_value(order_data["metro_station"])
        self.order_page.check_telephone_value(order_data["telephone"])

        print("Clicking the next button")
        self.order_page.click_next_button()

        print("Navigating to rent page")
        self.rent_page.set_when_to_deliver_today()  # Выбор текущей даты
        self.rent_page.select_rental_period(order_data["rental_period"])  # Пример выбора срока аренды

        if order_data["color_option"] == "black":
            self.rent_page.select_black_color()
        elif order_data["color_option"] == "grey":
            self.rent_page.select_grey_color()
        self.rent_page.set_courier_comment(order_data["courier_comment"])
        self.rent_page.click_order_button()

        print("Confirming the order")
        self.rent_page.confirm_order()
