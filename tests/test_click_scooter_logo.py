import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators
from config import MAIN_URL, ORDER_URL



@pytest.mark.usefixtures("setup")
class TestClickAlternateOrderButton:
    driver: webdriver.Firefox

    def scroll_to_alternate_order_button(self):
        element = self.driver.find_element(*MainPageLocators.alternate_order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def test_click_alternate_order_button(self):
        self.scroll_to_alternate_order_button()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.alternate_order_button)
        ).click()

        # Ожидание загрузки страницы заказа
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(ORDER_URL)
        )

        # Найти элемент логотипа и кликнуть на него
        scooter_logo = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.logo_scooter)
        )
        scooter_logo.click()

        # Проверка перехода на главную страницу
        assert self.driver.current_url == MAIN_URL
