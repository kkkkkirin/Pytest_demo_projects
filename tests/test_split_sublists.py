import pytest
import allure

from enums.enums_messages import EnumsErrors
from tasks.task3_split_in_sublists import split_into_sublists

@pytest.mark.split_to_sublists
@allure.feature("Task 3. Split to sublists function.")
class TestSplitIntoSublists:

    @allure.title("Positive test with valid values")
    @pytest.mark.parametrize(("input_list", "chunk_size", "expected"), [
        ([1, 2, 3, 4, 5, 6, 7, 8], 4, [[1, 2, 3, 4], [5, 6, 7, 8]]),
        (["sa", "dqw", "a", "bvv", "qp", "hgadd", "xsgh"], 2, [["sa", "dqw"], ["a", "bvv"], ["qp", "hgadd"], ["xsgh"]]),
        ([12,5,17, 1, 6, 8], 5, [[12,5,17, 1, 6,], [8]])
    ])
    def test_split_sublists(self, input_list, chunk_size, expected):
        with allure.step(f"Entered list: '{input_list}', and list divisor: {chunk_size}, the expected answer: '{expected}'"):
            assert split_into_sublists(input_list, chunk_size) == expected


    @allure.title("Negative test with invalid values instead of list")
    @pytest.mark.parametrize(("input_list", "chunk_size", "expected"), [
        ("a25fx1rf3g2v", 4, EnumsErrors.INVALID_TYPE_EXCEPT_LIST),
        (312512315124, 5, EnumsErrors.INVALID_TYPE_EXCEPT_LIST),
        (True, 2, EnumsErrors.INVALID_TYPE_EXCEPT_LIST)
    ])
    def test_input_not_lists(self, input_list, chunk_size, expected):
        with allure.step(f"Entered list: '{input_list}', list divisor: {chunk_size}, the expected error message: '{expected}'"):
            with pytest.raises(expected): split_into_sublists(input_list, chunk_size)


    @allure.title("Test with empty list")
    @allure.step("Empty value")
    def test_empty_list(self):
        assert split_into_sublists([], 3) == []

    @allure.title("Test with mixed values in list")
    def test_mixed_values(self):
        inp_list = ["at", 41, True, 5, "[w", -4]
        out_list = [["at", 41, True, 5], ["[w", -4]]

        with allure.step(f"The mixed list: '{inp_list}', divisor: 4, the result: '{out_list}'"):
            assert split_into_sublists(inp_list, 4) == out_list