import re

import allure

from enums.enums_messages import EnumsErrors

def count_words(text):
    if isinstance(text, str):
        clear_text = re.sub(r'[^\w\s]', '', text)
        return len(clear_text.strip().split())
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_STRING