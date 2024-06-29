import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators



@pytest.mark.usefixtures("setup")
class TestYandexLogoNavigation:
    driver: webdriver.Firefox

    def test_click_yandex_logo(self):
        yandex_logo_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.yandex_logo)
        )
        yandex_logo_element.click()

        # Ждем появления новой вкладки (если ссылка открылась в новой вкладке)
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))

        # Переключаемся на новую вкладку, если такая имеется
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])

        # Ждем, пока страница не загрузится и URL не изменится
        WebDriverWait(self.driver, 50).until(
            EC.url_contains("dzen.ru/?yredirect=true")
        )

        # Проверяем, что текущий URL содержит "dzen.ru=true"
        assert "dzen.ru/?yredirect=true" in self.driver.current_url.lower(), "Expected to navigate to Dzen page"





