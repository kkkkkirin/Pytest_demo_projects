import pytest
import allure

from enums.enums_messages import EnumsErrors
from tasks.task4_count_words import count_words

@allure.feature("Task 4. Counting words in sentence")
@pytest.mark.count_words
class TestCountWords:

    @pytest.mark.parametrize(("text", "expected"), [
        ("Lorem ipsum is simply dummy text", 6),
        ("That string ! to check, how func [] work with symbols .", 9),
        ("  Hello, world    ", 2)
    ])
    def test_count_words(self, text, expected):
        with allure.step(f"The entered text: '{text}', the count of words: {expected}"):
            assert count_words(text) == expected

    def test_count_words_with_empty_arg(self):
        assert count_words("") == 0

    def test_count_words_with_invalid_args(self):
        with pytest.raises(EnumsErrors.INVALID_TYPE_EXCEPT_STRING): count_words(125)
        with pytest.raises(EnumsErrors.INVALID_TYPE_EXCEPT_STRING): count_words(["aaa", "dc", "51sgf"])
