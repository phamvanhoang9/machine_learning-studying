
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1
        return index
    
if __name__ == "__main__":
    s = Solution()
    nums = [3, 2, 2, 3, 4, 5, 7]
    val = 3
    print(s.removeElement(nums, val))