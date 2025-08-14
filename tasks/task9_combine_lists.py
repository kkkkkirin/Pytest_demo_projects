from enums.enums_messages import EnumsErrors

def combine_lists(list1, list2):
    if isinstance(list1, list) and isinstance(list2, list):
        return list1 + list2
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_LIST