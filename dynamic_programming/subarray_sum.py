""" 
Given an unsorted array A of size N that contains only non negative integers, find a continuous sub-array that adds to a given number S and return the left and right index(1-based indexing) of that subarray.

In case of multiple subarrays, return the subarray indexes which come first on moving from left to right.

Note:- You have to return an ArrayList consisting of two elements left and right. In case no such subarray exists return an array consisting of element -1.

Your Task:
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N, and S as input parameters and returns an ArrayList containing the starting
and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the array should be according to 1-based indexing. If no such subarray is found,
return an array consisting of only one element that is -1.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

def subarraySum(arr, n, s):
    left = 0
    right = 0
    curr_sum = 0
    while right < n:
        curr_sum += arr[right]
        while curr_sum > s and left <= right:
            curr_sum -= arr[left]
            left += 1
        if curr_sum == s:
            return [left+1, right+1]
        right += 1
    return [-1]

# The above code has O(n) time complexity and O(1) space complexity. It uses two pointers to keep track of the subarray.
# The left pointer is used to keep track of the start of the subarray and the right pointer is used to keep track of the end of the subarray.
# The sum of the subarray is calculated and if it is greater than the given sum, the left pointer is incremented and the sum is reduced by the value at the left pointer.
# If the sum is equal to the given sum, the left and right pointers are returned as the answer.
# If no such subarray exists, [-1] is returned.

# Example
arr = [1, 2, 3, 7, 5]
n = 5
s = 12
print(subarraySum(arr, n, s)) # Output: [2, 4]