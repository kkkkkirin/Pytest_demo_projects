from enums.enums_messages import EnumsErrors

def calculate_even_sum(input_list):
    if isinstance(input_list, list):
        counter = 0
        for item in input_list:
            if isinstance(item, int):
                if item % 2 == 0:
                    counter += item
            else: return EnumsErrors.INVALID_TYPE_EXCEPT_INT
        return counter
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_LIST