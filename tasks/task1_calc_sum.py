from enums.enums_messages import EnumsErrors

def calculate_sum(N):
    if isinstance(N, int):
        if N < 0: return EnumsErrors.NEGATIVE_VALUE
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_INT

    return sum(i for i in range(N + 1))
