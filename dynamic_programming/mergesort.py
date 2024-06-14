import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])


def mergesort(values):
    if len(values) <= 1:
        return values
    
    mid = len(values) // 2
    left = mergesort(values[:mid])
    right = mergesort(values[mid:])
    sorted_values = []
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            sorted_values.append(left[left_idx])
            left_idx += 1
        else:
            sorted_values.append(right[right_idx])
            right_idx += 1

    sorted_values += left[left_idx:]
    sorted_values += right[right_idx:]

    return sorted_values

print(mergesort(numbers))