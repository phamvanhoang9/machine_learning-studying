"""
Quick sort algorithm:
    1. Pick a pivot
    2. Partition the array into two subarrays: elements less than the pivot and elements greater than the pivot
    3. Recursively sort the two subarrays
"""

# Basic code
def quick_sort(arr, left, right):
    if left < right:
        partition_pos = partition(arr, left, right)
        quick_sort(arr, left, partition_pos - 1)
        quick_sort(arr, partition_pos + 1, right)

    return arr

def partition(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] >= pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]
    
    return i 


# Advanced code
def advanced_quick_sort(arr, left, right):
    if left < right:
         pivot_pos = new_partition(arr, left, right)
         advanced_quick_sort(arr, left, pivot_pos - 1)
         advanced_quick_sort(arr, pivot_pos + 1, right)
    
    return arr

def new_partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[right] = arr[right], arr[i + 1]

    return i + 1


arr = [33, 22, 77, 11, 66, 44, 55]
print(advanced_quick_sort(arr, 0, len(arr) - 1))

# print(quick_sort(arr, 0, len(arr) - 1))