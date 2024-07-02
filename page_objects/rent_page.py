from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RentPageLocators


class RentPage:
    def __init__(self, driver):
        self.driver = driver

    def set_when_to_deliver_today(self):
        # Открытие календаря
        print("Clicking on the delivery date field to open the calendar")
        calendar_icon = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.when_to_deliver_field)
        )
        calendar_icon.click()
        print("Calendar opened")

        # Ожидание загрузки календаря и выбор сегодняшней даты
        print("Waiting for the calendar to be clickable")
        today_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.calendar_today)
        )
        today_element.click()
        print("Today's date selected")

    def select_rental_period(self, period):
        print("Selecting rental period")
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.rental_period_dropdown)
        )
        dropdown.click()
        print("Rental period dropdown clicked")

        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, RentPageLocators.rental_period_option[1].format(period)))
        )
        option.click()
        print("Rental period selected")

    def select_black_color(self):
        print("Selecting black color option")
        color_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.black_color_option)
        )
        color_option.click()
        print("Black color selected")

        # Добавляем выбор серого цвета

    def select_grey_color(self):
        print("Selecting grey color option")
        color_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.grey_color_option)
        )
        color_option.click()
        print("Grey color selected")

    def set_courier_comment(self, comment):
        print("Entering courier comment")
        comment_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(RentPageLocators.courier_comment_field)
        )
        comment_field.clear()
        comment_field.send_keys(comment)
        print("Courier comment entered")

    def click_order_button(self):
        print("Clicking the order button")
        order_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.RENT_PAGE_ORDER_BUTTON)
        )
        order_button.click()
        print("Order button clicked")

    def confirm_order(self):
        print("Clicking the confirm button")
        confirm_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(RentPageLocators.ORDER_CONFIRMATION_MODAL_YES_BUTTON)
        )
        confirm_button.click()
        print("Order confirmed")











