import pytest
from page_objects.main_page import MainPage

@pytest.mark.usefixtures("driver")
class TestFAQ:
    @pytest.mark.parametrize("question_index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_questions(self, question_index, driver):
        main_page = MainPage(driver)
        main_page.open_question(question_index)
        assert main_page.get_answer_text(question_index) != ""


































