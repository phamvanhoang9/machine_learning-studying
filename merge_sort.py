"""
Merge sort algorithm:
    1. Divide the array into two halves
    2. Recursively sort the two halves
    3. Merge the two halves
"""
from typing import List

# Intermediate level
def merge_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

# Advanced level
def advanced_merge(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_arr = advanced_merge(array[:mid])
    right_arr = advanced_merge(array[mid:])

    i = j = 0
    merged = []

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1
    
    merged.extend(left_arr[i:])
    merged.extend(right_arr[j:])

    return merged


array = [3, 4, 1, 2, 5, 7, 6, 7, 4]
# print(merge_sort(array))
print(advanced_merge(array))
