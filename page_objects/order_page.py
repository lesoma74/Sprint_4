from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import OrderFormLocators



class OrderForm:
    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*OrderFormLocators.name_field).send_keys(name)

    def set_last_name(self, last_name):
        self.driver.find_element(*OrderFormLocators.last_name_field).send_keys(last_name)

    def set_address(self, address):
        self.driver.find_element(*OrderFormLocators.address_field).send_keys(address)

    def set_metro_station(self, metro_station):
        metro_station_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(OrderFormLocators.metro_station_field)
        )
        metro_station_element.click()

        # Ожидание пока выпадающий список станет видимым и выбор опции
        option_locator = (By.XPATH, OrderFormLocators.metro_station_option[1].format(metro_station))
        option_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(option_locator)
        )
        option_element.click()

    def set_telephone(self, telephone):
        self.driver.find_element(*OrderFormLocators.telephone_field).send_keys(telephone)

    def click_next_button(self):
        self.driver.find_element(*OrderFormLocators.next_button).click()

    def check_name_value(self, name):
        actually_value = self.driver.find_element(*OrderFormLocators.name_field).get_property("value")
        assert actually_value == name, f'Ожидалось значение поля name: "{name}", получено "{actually_value}"'

    def check_last_name_value(self, last_name):
        actually_value = self.driver.find_element(*OrderFormLocators.last_name_field).get_property("value")
        assert actually_value == last_name, f'Ожидалось значение поля last_name: "{last_name}", получено "{actually_value}"'

    def check_address_value(self, address):
        actually_value = self.driver.find_element(*OrderFormLocators.address_field).get_property("value")
        assert actually_value == address, f'Ожидалось значение поля address: "{address}", получено "{actually_value}"'

    def check_metro_station_value(self, metro_station):
        actually_value = self.driver.find_element(*OrderFormLocators.metro_station_field).get_property("value")
        assert actually_value == metro_station, f'Ожидалось значение поля metro_station: "{metro_station}", получено "{actually_value}"'

    def check_telephone_value(self, telephone):
        actually_value = self.driver.find_element(*OrderFormLocators.telephone_field).get_property("value")
        assert actually_value == telephone, f'Ожидалось значение поля telephone: "{telephone}", получено "{actually_value}"'






