import pytest
import allure

from tasks.task7_smallest_prime_devisor import smallest_prime_devisor
from enums.enums_messages import EnumsErrors

@pytest.mark.smallest_divisor
@allure.feature("Task 7. Function to search the smallest divisor")
class TestSmallestDivisor:

    @allure.title("Positive test with valid values")
    @pytest.mark.parametrize(("n", "expected"), [
        (42, 2),
        (11, 11),
        (21, 3),
        (241, 241),
        (79, 79)
    ])
    def test_smallest_divisor(self, n, expected):
        with allure.step(f"Entered number: {n}, the expected result: {expected}"):
            assert smallest_prime_devisor(n) == expected


    @allure.title("Negative test with invalid values")
    @pytest.mark.parametrize(("n", "expected"), [
        (1, EnumsErrors.SMALL_VALUE),
        (0, EnumsErrors.SMALL_VALUE),
        (-5, EnumsErrors.NEGATIVE_VALUE),
        ("6", EnumsErrors.INVALID_TYPE_EXCEPT_INT),
        ([26], EnumsErrors.INVALID_TYPE_EXCEPT_INT)
    ])
    def test_smallest_divisor_invalid_values(self, n, expected):
        with allure.step(f"Entered number:{n}"):
            with pytest.raises(expected): smallest_prime_devisor(n)
