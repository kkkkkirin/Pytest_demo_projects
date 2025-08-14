from enums.enums_messages import EnumsErrors

def are_anagrams(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        str1_chars = sorted([item for item in str1.strip() if item != ' '])
        str2_chars = sorted([item for item in str2.strip() if item != ' '])
        if len(str1_chars) == len(str2_chars):
            if str1_chars == str2_chars: return True
            else: return False
        else: return False
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_STRING