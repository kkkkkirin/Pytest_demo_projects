import pytest
import allure

from enums.enums_messages import EnumsErrors
from tasks.task2_calc_even_sum import calculate_even_sum

@pytest.mark.calc_even_sum
@allure.feature("Task 2. Counting the sum of even numbers function")
class TestCalcEvenSum:

    @allure.title("Positive test with valid values")
    @pytest.mark.parametrize(("input_list", "expected"), [
        ([0, 2, 5, 6, 7], 8),
        ([12, 5, 4, 1, 15], 16),
        ([11, 5, 3, 1, 15], 0),
        ([], 0)
    ])

    def test_calc_even_sum_with_positive_values(self, input_list, expected):
        with allure.step(f"Entered list: '{input_list}', the expected answer: '{expected}'"):
            assert calculate_even_sum(input_list) == expected


    @allure.title("Positive test with negative elements in list")
    @pytest.mark.parametrize(("input_list", "expected"), [
        ([-4, -2, -5, -1, 0, -6], -12),
        ([-6, 2, 1, 2, -5], -2),
        ([-11, -5, -3, -1, -3], 0)
    ])
    def test_calc_even_sum_with_negative_values(self, input_list, expected):
        with allure.step(f"Entered list: '{input_list}', the expected answer: '{expected}'"):
            assert calculate_even_sum(input_list) == expected


    @allure.title("Negative test with invalid lists or elements")
    @pytest.mark.parametrize(("input_list", "expected"), [
        (12, EnumsErrors.INVALID_TYPE_EXCEPT_LIST),
        (["wsa", "y6", "12"], EnumsErrors.INVALID_TYPE_EXCEPT_INT),
        (["12","25","5","2"], EnumsErrors.INVALID_TYPE_EXCEPT_INT)
    ])
    def test_calc_even_sum_invalid_values(self, input_list, expected):
        with allure.step(f"The entered list: {input_list}, the expected error message: {expected}"):
            with pytest.raises(expected): calculate_even_sum(input_list)
