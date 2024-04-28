from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        currEnd = 0
        currFarthest = 0

        for i in range(len(nums)-1):
            currFarthest = max(currFarthest, i + nums[i])
            if (i == currEnd):
                jumps += 1
                currEnd = currFarthest

        return jumps

if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    print(s.jump(nums=nums))