from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[k] = nums[i]
                k += 1

        return k # return the number of elements are not duplication
    
if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 0, 1, 1, 2, 4, 6, 7, 7]
    print(s.removeDuplicates(nums))