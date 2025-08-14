import pytest
import allure

from tasks.task1_calc_sum import calculate_sum
from enums.enums_messages import EnumsErrors

@pytest.mark.calc_sum
@allure.feature("Task 1. Counting the sum of numbers function")
class TestCalculationSum:

    @allure.title("Positive test with valid numbers")
    @pytest.mark.parametrize(("N", "expected"), [
        (0, 0),
        (5, 15),
        (100, 5050)
    ])
    def test_calc_sum_positive(self, N, expected):
        with allure.step(f"Entered number: {N}, expected result: {expected}"):
            assert calculate_sum(N) == expected


    @allure.title("Negative test with invalid values")
    @pytest.mark.parametrize(("N", "expected"), [
        (-5, EnumsErrors.NEGATIVE_VALUE),
        ("24", EnumsErrors.INVALID_TYPE_EXCEPT_INT),
        ("cvq", EnumsErrors.INVALID_TYPE_EXCEPT_INT),
    ])
    def test_calc_sum_negative(self, N, expected):
        with allure.step(f"Entered value: '{N}', expected error message: {expected}"):
            with pytest.raises(expected): calculate_sum(N)
