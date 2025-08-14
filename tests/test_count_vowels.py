import allure
import pytest

from tasks.task10_count_vowels import count_vowels
from enums.enums_messages import EnumsErrors

@pytest.mark.count_vowels
@allure.feature("Task 10. Function to count vowels in string")

class TestCountVowels:

    @allure.title("Positive test with valid values")
    @pytest.mark.parametrize(("input_str", "expected"), [
        ("string", 1),
        ("HELLO", 2),
        ("NeW SentencE", 4),
        ("24512", 0)
    ])
    def test_count_vowels(self, input_str, expected):
        with allure.step(f"Entered string: '{input_str}', the expected result: {expected}"):
            assert count_vowels(input_str) == expected

    @allure.title("Negative test with invalid values")
    @pytest.mark.count_vowels
    def test_count_vowels_invalid_values(self):
        with pytest.raises(EnumsErrors.INVALID_TYPE_EXCEPT_STRING): count_vowels(12)
        with pytest.raises(EnumsErrors.INVALID_TYPE_EXCEPT_STRING): count_vowels(["world"])
