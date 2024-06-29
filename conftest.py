import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from page_objects.order_page import OrderForm
from page_objects.rent_page import RentPage

@pytest.fixture(scope="class")
def setup(request):
    print("Setting up the driver and page objects")
    options = webdriver.FirefoxOptions()
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    order_page = OrderForm(driver)
    rent_page = RentPage(driver)

    request.cls.driver = driver
    request.cls.order_page = order_page
    request.cls.rent_page = rent_page

    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield
    driver.quit()
    print("Teardown: Closing the driver")

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()



