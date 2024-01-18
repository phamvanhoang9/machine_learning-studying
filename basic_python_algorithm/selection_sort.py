"""
Selection sort algorithm:
    1. Find the smallest element in the array
    2. Swap it with the first element in the array
    3. Repeat the process with the remaining array
"""
from typing import List

def selection_sort(array):
    if not isinstance(array, List):
        raise TypeError("The input array must be a list")
    
    if len(array) <= 1:
        return array
    
    for i in range(0, len(array) - 1):
        current_min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[current_min_index]:
                current_min_index = j
        
        array[i], array[current_min_index] = array[current_min_index], array[i]

    return array


array1 = (2, 8, 4, 1, 7, 6, 5, 3)
array = [9, 6, 7, 5, 4, 8]
print(selection_sort(list(array1)))