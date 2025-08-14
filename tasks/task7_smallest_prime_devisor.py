import math

from enums.enums_messages import EnumsErrors

def smallest_prime_devisor(n):
    if isinstance(n, int):
        if n > 1:
            if n % 2 == 0: return 2

            for i in range(3, int(math.sqrt(n)) + 1, 2):
                if n % i == 0:
                    return i

            return n

        else:
            if n == 0 or n == 1: return EnumsErrors.SMALL_VALUE
            else: return EnumsErrors.NEGATIVE_VALUE
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_INT

