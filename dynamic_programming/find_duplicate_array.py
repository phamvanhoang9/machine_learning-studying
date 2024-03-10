"""
Given an array a of size N which contains elements from 0 to N-1, you need to find all the elements occurring more than once in the given array. 
Return the answer in ascending order. If no such element is found, return list containing [-1]. 

Complete the function duplicates() which takes array a[] and n as input as parameters and returns a list of elements that occur more than once in the given array in a sorted manner. 

Expected Time Complexity: O(n).
Expected Auxiliary Space: O(n).
"""

# class Solution:
#     def duplicates(self, arr, n):
#         ans = []
#         seen = set()
#         for num in arr:
#             if num in seen and num not in ans:
#                 ans.append(num)
#             seen.add(num)
#         return sorted(ans) if ans else [-1]
    
class Solution:
    def duplicates(self, arr, n):
        frequency = {}
        ans = []

        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num, count in frequency.items():
            if count > 1:
                ans.append(num)
            
        return sorted(ans) if ans else [-1]
    
    
if __name__ == "__main__":
    print("Enter n number:")
    n = int(input())
    print("Enter the n list of numbers:")
    arr = list(map(int, input().strip().split()))
    res = Solution().duplicates(arr, n)
    print(res)