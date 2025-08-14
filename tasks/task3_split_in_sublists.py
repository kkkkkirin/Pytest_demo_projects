import allure

from enums.enums_messages import EnumsErrors

def split_into_sublists(input_list, chunk_size):
    if isinstance(input_list, list):
        output_list = []
        for item in range(0, len(input_list), chunk_size):
             output_list += [input_list[item : item + chunk_size]]
        return output_list
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_LIST