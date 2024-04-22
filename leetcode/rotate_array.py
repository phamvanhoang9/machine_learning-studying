from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> List:
        for _ in range(k):
            self.reverse(nums)

        return nums
    
    def reverse(self, nums: List[int]) -> List:
        i, end = 0, len(nums) - 1
        while i < end:
            nums[i], nums[end] = nums[end], nums[i]
            i += 1

        return nums
    
if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 4, 5]
    k = 3
    print(s.rotate(nums, k))