"""
Linear Search Algorithm
- Linear search is a very simple search algorithm.
- In this type of search, a sequential search is made over all items one by one.
- Every item is checked and if a match is found then that particular item is returned, otherwise the search continues till the end of the data collection.
- Linear search is rarely used practically because other search algorithms such as the binary search algorithm and hash tables allow significantly faster searching comparison to Linear search.
- Linear search operates in O(n) time complexity, where n is the number of elements in the list.
"""

from typing import List, Any

def linear_search(arr: List[Any], target: Any) -> int:
    """
    Linear search algorithm
    - Time complexity: O(n)
    - Space complexity: O(1)
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Test cases
assert(linear_search([1, 2, 3, 4, 5], 3) == 2)
assert(linear_search([1, 2, 3, 4, 5], 6) == -1)
assert(linear_search([1, 2, 3, 4, 5], 1) == 0)

print("Linear search algorithm passed")
