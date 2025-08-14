from enums.enums_messages import EnumsErrors

def find_unique(input_list):
    if isinstance(input_list, list):
        counts = {}

        for item in input_list:
            counts[item] = counts.get(item, 0) + 1

        return [elem for elem, count in counts.items() if count == 1]
    else: return EnumsErrors.INVALID_TYPE_EXCEPT_LIST


numbers = [1, 2, 2, 3, 3, 4, 5]
unique_numbers = find_unique(numbers)
print(unique_numbers)
