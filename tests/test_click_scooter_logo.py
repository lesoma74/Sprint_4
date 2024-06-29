import pytest
import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators



@pytest.mark.usefixtures("setup")
class TestClickAlternateOrderButton:
    driver: webdriver.Firefox

    def scroll_to_alternate_order_button(self):
        element = self.driver.find_element(*MainPageLocators.alternate_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def test_click_alternate_order_button(self):
        self.scroll_to_alternate_order_button()
        time.sleep(2)  # Задержка на 2 секунды

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.alternate_order_button)
        ).click()

        # Ожидание загрузки страницы заказа
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("https://qa-scooter.praktikum-services.ru/order")
        )

        # Найти элемент логотипа и кликнуть на него
        scooter_logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.logo_scooter)
        )
        scooter_logo.click()

        # Проверка перехода на главную страницу
        assert self.driver.current_url == "https://qa-scooter.praktikum-services.ru/"
