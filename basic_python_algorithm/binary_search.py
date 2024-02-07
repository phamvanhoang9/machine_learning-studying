from typing import List, Any

def binary_search(arr: List[Any], target: Any) -> int:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return None

# Test case
array = [4, 5, 6, 7, 8, 9]
print(binary_search(array, 10))