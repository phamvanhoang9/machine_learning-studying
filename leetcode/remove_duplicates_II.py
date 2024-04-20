from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 2
        for j in range(2, len(nums)):
            if nums[j] != nums[k-2]:
                nums[k] = nums[j]
                k += 1
        return k, nums
    
if __name__ == "__main__":
    s = Solution()
    nums = [1, 1, 1, 2, 3, 3, 4, 4, 4, 5, 5, 5]
    print(s.removeDuplicates(nums))
