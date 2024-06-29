
from page_objects.main_page import MainPage


class TestFAQ:
    def test_question1(self, driver):
        main_page = MainPage(driver)
        main_page.open_question(0)
        assert main_page.get_answer_text(0) != ""

    def test_question2(self, driver):
        main_page = MainPage(driver)
        main_page.open_question(1)
        assert main_page.get_answer_text(1) != ""

    def test_question3(self, driver):
        main_page = MainPage(driver)
        main_page.open_question(2)
        assert main_page.get_answer_text(2) != ""

    def test_question4(self, driver):
        main_page = MainPage(driver)
        main_page.open_question(3)
        assert main_page.get_answer_text(3) != ""

    def test_question5(self, driver):
        main_page = MainPage(driver)
        main_page.open_question(4)
        assert main_page.get_answer_text(4) != ""

    def test_question6(self, driver):
        main_page = MainPage(driver)
        main_page.open_question(5)
        assert main_page.get_answer_text(5) != ""

    def test_question7(self, driver):
        main_page = MainPage(driver)
        main_page.open_question(6)
        assert main_page.get_answer_text(6) != ""

    def test_question8(self, driver):
        main_page = MainPage(driver)
        main_page.open_question(7)
        assert main_page.get_answer_text(7) != ""































