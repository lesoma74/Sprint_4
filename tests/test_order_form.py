import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.order_page import OrderForm
from page_objects.rent_page import RentPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, RentPageLocators

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
            EC.url_to_be("https://qa-scooter.praktikum-services.ru/order")
        )

    def test_fill_order_form(self):
        self.navigate_to_order_page()
        print("Filling out the order form")
        self.order_page.set_name("Иван")
        self.order_page.set_last_name("Иванов")
        self.order_page.set_address("Москва, ул. Пушкина, д. Колотушкина")
        self.order_page.set_metro_station("Пушкинская")
        self.order_page.set_telephone("+79991234567")

        print("Checking the field values")
        self.order_page.check_name_value("Иван")
        self.order_page.check_last_name_value("Иванов")
        self.order_page.check_address_value("Москва, ул. Пушкина, д. Колотушкина")
        self.order_page.check_metro_station_value("Пушкинская")
        self.order_page.check_telephone_value("+79991234567")

        print("Clicking the next button")
        self.order_page.click_next_button()

        print("Navigating to rent page")
        self.rent_page.set_when_to_deliver_today()  # Выбор текущей даты
        self.rent_page.select_rental_period("двое суток")  # Пример выбора срока аренды
        self.rent_page.select_black_color()
        self.rent_page.set_courier_comment("Без звонка")
        self.rent_page.click_order_button()

        print("Confirming the order")
        self.rent_page.confirm_order()

    @pytest.mark.parametrize("name, last_name, address, metro_station, telephone, rental_period, courier_comment, color_option", [
        ("Петр", "Петров", "Санкт-Петербург, ул. Ленина, д. Дом", "Комсомольская", "+79997654321", "трое суток", "Звонить заранее", "black"),
        ("Сергей", "Сергеев", "Москва, ул. Лесная, д. 10", "Арбатская", "+79996543210", "четверо суток", "Звонить вечером", "grey")
    ])
    def test_fill_order_form_with_new_data(self, name, last_name, address, metro_station, telephone, rental_period, courier_comment, color_option):
        print("Re-opening the browser")
        self.driver.get("https://qa-scooter.praktikum-services.ru/")

        self.navigate_to_order_page()
        print(f"Filling out the order form with new data: {name}, {last_name}, {address}, {metro_station}, {telephone}")
        self.order_page.set_name(name)
        self.order_page.set_last_name(last_name)
        self.order_page.set_address(address)
        self.order_page.set_metro_station(metro_station)
        self.order_page.set_telephone(telephone)

        print("Checking the field values")
        self.order_page.check_name_value(name)
        self.order_page.check_last_name_value(last_name)
        self.order_page.check_address_value(address)
        self.order_page.check_metro_station_value(metro_station)
        self.order_page.check_telephone_value(telephone)

        print("Clicking the next button")
        self.order_page.click_next_button()

        print("Navigating to rent page")
        self.rent_page.set_when_to_deliver_today()  # Выбор текущей даты
        self.rent_page.select_rental_period(rental_period)  # Пример выбора срока аренды

        if color_option == "black":
            self.rent_page.select_black_color()
        elif color_option == "grey":
            self.rent_page.select_grey_color()
        self.rent_page.set_courier_comment(courier_comment)
        self.rent_page.click_order_button()

        print("Confirming the order")
        self.rent_page.confirm_order()



