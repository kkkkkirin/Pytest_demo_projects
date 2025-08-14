import pytest
import allure

from enums.enums_messages import EnumsErrors
from tasks.task5_find_unique_elem import find_unique

@allure.feature("Task 5. Find unique elements function")
@pytest.mark.find_unique_elem
class TestFindUniqueElements:

    @pytest.mark.parametrize(("input_list", "expected"), [
        ([1, 1, 2, 3, 3, 5, 2], [5]),
        ([1, -1, 2, 3, 3, 5, 2], [1, -1, 5]),
        (['aa', 'abc', 'bb', 'abc'], ['aa', 'bb'])
    ])
    def test_find_unique_values(self, input_list, expected):
        with allure.step(f"Entered list: '{input_list}', the expected result: '{expected}'"):
            assert find_unique(input_list) == expected

    def test_with_empty_arg(self):
        assert find_unique([]) == []

    def test_with_invalid_values(self):
        with pytest.raises(EnumsErrors.INVALID_TYPE_EXCEPT_LIST): find_unique(512)
        with pytest.raises(EnumsErrors.INVALID_TYPE_EXCEPT_LIST): find_unique({12, 12, 51, 61})

    def test_with_mixed_values(self):
        inp_list = [12, "hello", 5, 2, 2, "world", 9, "hello", False]
        out_list = [12, 5, "world", 9, False]

        with allure.step(f"Entered list: '{inp_list}', the expected result: '{out_list}'"):
            assert find_unique(inp_list) == out_list