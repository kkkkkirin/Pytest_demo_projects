import pytest
import allure

from enums.enums_messages import EnumsErrors
from tasks.task9_combine_lists import combine_lists

@pytest.mark.combine_lists
@allure.feature("Task 9. Function to combine lists")
class TestCombineLists:

    @allure.title("Positive test with valid lists")
    @pytest.mark.parametrize(("list1", "list2", "expected"), [
        (["hello"], ["world", "!"], ["hello", "world", "!"]),
        ([52, 71, 4], [12, 51, 6], [52, 71, 4, 12, 51, 6]),
        ([{1: "he", 2: "llo"}], [{4: "wor", 5: "ld"}], [{1: "he", 2: "llo"}, {4: "wor", 5: "ld"}]),
    ])
    def test_combine_lists(self, list1, list2, expected):
        with allure.step(f"Entered lists: '{list1}' and '{list2}', the expected result: {expected}"):
            assert combine_lists(list1, list2) == expected


    @allure.title("Negative test with invalid values")
    @pytest.mark.parametrize(("list1", "list2", "expected"), [
        (24, [5], EnumsErrors.INVALID_TYPE_EXCEPT_LIST),
        ({21,4, 6}, {65, "qwerty"}, EnumsErrors.INVALID_TYPE_EXCEPT_LIST)
    ])
    def test_combine_lists_invalid_values(self, list1, list2, expected):
        with allure.step(f"Entered values: '{list1}' and '{list2}'"):
            with pytest.raises(expected): combine_lists(list1, list2)


    @allure.title("Test with mixed values")
    @pytest.mark.parametrize(("list1", "list2", "expected"), [
        ([24, 531], ["qwerty", "hi"], [24, 531, "qwerty", "hi"]),
        ([[24, "5"], "hello"], [12, 0], [[24, "5"], "hello", 12, 0])
    ])
    def test_combine_lists_with_mixed_values(self, list1, list2, expected):
        with allure.step(f"Entered lists: '{list1}' and '{list2}', the expected result: {expected}"):
            assert combine_lists(list1, list2) == expected


    @allure.title("Test with empty lists")
    def test_combine_lists_with_empty_value(self):
        assert combine_lists([], []) == []