from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_important_questions(self):
        element = self.driver.find_element(*MainPageLocators.important_questions_header)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def open_question(self, question_index):
        self.scroll_to_important_questions()  # Скролл до "Вопросы о важном"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.question_locators[question_index])
        ).click()

    def get_answer_text(self, question_index):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.answer_locators[question_index])
        ).text


















