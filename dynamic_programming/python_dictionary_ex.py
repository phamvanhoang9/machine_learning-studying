
from typing import List


def faster_counter(string: str) -> dict:
    counter = {}
    string = string.lower()
    for letter in string:
        if letter.isalpha():
            counter[letter] = counter.get(letter, 0) + 1 # default = 0 or increment for each letter

    return counter

def merge_dict(dict1: dict, dict2: dict) -> dict:
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict


# Check duplication for each string
def has_duplicates(sequence: str|List) -> bool:
    seen = set() # using set to keep track of the items it has seen so far
    for item in sequence:
        if item in seen:
            return True
        seen.add(item)

    return False

def is_interlocking(word: str, word_list: set) -> bool:
        first = word[0::2]
        second = word[1::2]

        return first in word_list and second in word_list

# print(merge_dict(faster_counter("stevehoang"), faster_counter("hanoiuniversity")))
# print(has_duplicates("unpredictably"))
# print(has_duplicates([1, 2, 4, 5, 3, 6, 5, 7]))
word_list = set(["steve", "hoang", "hanoi", "university", "shoe", "cold"])
print(is_interlocking("stevehoang", word_list=word_list))
print(is_interlocking("schooled", word_list))