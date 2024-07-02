from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локаторы вопросов
    question_locators = [
        (By.CSS_SELECTOR, "#accordion__heading-0"),
        (By.CSS_SELECTOR, "#accordion__heading-1"),
        (By.CSS_SELECTOR, "#accordion__heading-2"),
        (By.CSS_SELECTOR, "#accordion__heading-3"),
        (By.CSS_SELECTOR, "#accordion__heading-4"),
        (By.CSS_SELECTOR, "#accordion__heading-5"),
        (By.CSS_SELECTOR, "#accordion__heading-6"),
        (By.CSS_SELECTOR, "#accordion__heading-7")
    ]

    # Локаторы ответов
    answer_locators = [
        (By.CSS_SELECTOR, "#accordion__panel-0 > p"),
        (By.CSS_SELECTOR, "#accordion__panel-1 > p"),
        (By.CSS_SELECTOR, "#accordion__panel-2 > p"),
        (By.CSS_SELECTOR, "#accordion__panel-3 > p"),
        (By.CSS_SELECTOR, "#accordion__panel-4 > p"),
        (By.CSS_SELECTOR, "#accordion__panel-5 > p"),
        (By.CSS_SELECTOR, "#accordion__panel-6 > p"),
        (By.CSS_SELECTOR, "#accordion__panel-7 > p")
    ]

    # Локатор для заголовка "Вопросы о важном"
    important_questions_header = (By.XPATH, "//*[contains(text(), 'Вопросы о важном')]")
    # Локатор для альтернативной кнопки Заказать
    alternate_order_button = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    # Локатор лого Самокат
    logo_scooter = (By.CSS_SELECTOR, "img[src='/assets/scooter.svg']")
    # Локатор лого Яндекс
    yandex_logo = (By.CSS_SELECTOR, ".Header_LogoYandex__3TSOI img")
    # Локатор для кнопки Заказать
    order_button = (By.CSS_SELECTOR, "button.Button_Button__ra12g")

class OrderFormLocators:
    name_field = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    last_name_field = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    address_field = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    metro_station_field = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    metro_station_option = (By.XPATH, "//div[@class='select-search__select']/ul/li/button/div[text()='{}']")
    telephone_field = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Middle__1CSJM")

class RentPageLocators:
    when_to_deliver_field = (By.CSS_SELECTOR, ".react-datepicker__input-container > input")
    calendar_today = (By.CSS_SELECTOR, ".react-datepicker__day--today")
    rental_period_dropdown = (By.CSS_SELECTOR, ".Dropdown-placeholder")
    rental_period_option = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")
    black_color_option = (By.ID, "black")
    grey_color_option = (By.ID, "grey")
    courier_comment_field = (By.CSS_SELECTOR, "input[placeholder='Комментарий для курьера']")
    RENT_PAGE_ORDER_BUTTON = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM:nth-of-type(2)")
    confirm_button = (By.CSS_SELECTOR, "button.Button_Button__ra12g.Button_Middle__1CSJM")
    confirm_order_button = (By.XPATH, "//button[contains(text(), 'Заказать')]")  # Локатор кнопки "Заказать"
    ORDER_CONFIRMATION_MODAL_YES_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]')
    order_confirmation_modal = (
    By.CSS_SELECTOR, ".Order_ModalHeader__3FDaJ")  # Локатор модального окна подтверждения заказа

