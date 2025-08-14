import allure
import pytest

from enums.enums_messages import EnumsErrors
from tasks.task8_are_anagrams import are_anagrams

@pytest.mark.are_anagrams
@allure.feature("Task 8. Function to check are strings are anagrams")
class TestAreAnagrams:

    @allure.title("Positive test with valid strings")
    @pytest.mark.parametrize(("str1", "str2", "expected"), [
        ("hello world", "hello world!", False),
        ("lorem ipsum", "remipsumlo", True),
        ("qwerty", "tytrewq", False),
        ("137", "3 1 7", True)
    ])
    def test_are_anagrams(self, str1, str2, expected):
        with allure.step(f"Enter the strings: '{str1}' and '{str2}', the expected result: {expected}"):
            assert are_anagrams(str1, str2) == expected

    @allure.title("Negative test with invalid values")
    @pytest.mark.parametrize(("str1", "str2", "expected"), [
        (132, 231,  EnumsErrors.INVALID_TYPE_EXCEPT_STRING),
        (["hello"], "elhlo", EnumsErrors.INVALID_TYPE_EXCEPT_STRING),
        ("452", 254, EnumsErrors.INVALID_TYPE_EXCEPT_STRING),
    ])
    def test_are_anagrams_invalid_values(self, str1, str2, expected):
        with allure.step(f"Enter the strings: '{str1}' and '{str2}', the expected result: {expected}"):
            with pytest.raises(expected): are_anagrams(str1, str2)
