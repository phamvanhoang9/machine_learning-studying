# Ex: array = [2, 8, 4, 1, 3, 7, 6, 5]
#    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8]

"""
Insertion sort algorithm:
    1. We need an outer loop from the second index
    2. We need an inner loop to compare the current value to the privious value
    3. We need to swap them if the current value is smaller than the privious value
"""

def insertion_sort(array):
    # We need an outer loop from the second index
    for i in range(1, len(array)):
        # an inter loop
        j = i
        # compare the current value to the privious value
        while array[j - 1] > array[j] and j > 0:
            # swap them
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1 # decrease the index to further comparing
    
    return array

def advanced_insertion(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

# Example:
array = [2, 8, 4, 1, 7, 6, 5, 3]
arr = [2, 8, 4, 1, 7, 6, 5, 3]
print(insertion_sort(array))
print(advanced_insertion(arr))
