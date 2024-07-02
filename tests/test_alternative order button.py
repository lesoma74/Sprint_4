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
        self.driver.get(MAIN_URL)
        self.scroll_to_alternate_order_button()

        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.alternate_order_button)
        ).click()

        # Проверяем URL с ожиданием, чтобы быть уверенным, что он загружен полностью
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be(ORDER_URL)
        )
        assert self.driver.current_url == ORDER_URL, f"Expected URL: {ORDER_URL}, but got: {self.driver.current_url}"
