from enums.enums_messages import EnumsErrors

VOWELS = ["a", "e", "i", "o", "u"]

def count_vowels(input_str):
    if isinstance(input_str, str):
        return sum(1 for char in input_str.lower() if char in VOWELS)
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_STRING

