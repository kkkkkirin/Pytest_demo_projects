import pytest
import allure

from tasks.task6_is_palindrome import is_palindrome
from enums.enums_messages import EnumsErrors

@pytest.mark.palindrome
@allure.feature("Task 6. Is number is palindrome function")
class TestPalindrome:

    @pytest.mark.parametrize(("num", "expected"), [
        (7, True),
        (42, False),
        (111, True),
        (785, False),
        (0, True)
    ])
    def test_palindrome(self, num, expected):
        with allure.step(f"Entered number: {num}, the expected answer: {expected}"):
            assert is_palindrome(num) == expected


    @pytest.mark.parametrize(("value", "expected"), [
        ("'25'", EnumsErrors.INVALID_TYPE_EXCEPT_INT),
        ("hello", EnumsErrors.INVALID_TYPE_EXCEPT_INT),
        ({11}, EnumsErrors.INVALID_TYPE_EXCEPT_INT),
        (-111, EnumsErrors.NEGATIVE_VALUE),
    ])
    def test_palindrome_invalid_values(self, value, expected):
        with allure.step(f"Entered value: {value}, the expected error message: '{expected}'"):
            with pytest.raises(expected): is_palindrome(value)