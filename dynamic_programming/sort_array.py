""" 
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
"""

def sortArray(arr, n):
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example
arr = [0, 2, 1, 2, 0]
n = 5

print(sortArray(arr, n)) # Output: [0, 0, 1, 2, 2]