from enums.enums_messages import EnumsErrors

def is_palindrome(num):
    if isinstance(num, int):
        if num >= 0:
            str_value = str(num)
            return str_value == str_value[::-1]
        else: return EnumsErrors.NEGATIVE_VALUE
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_INT