from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        m = defaultdict(int)
        
        for num in nums:
            m[num] += 1

        n = n // 2
        for key, value in m.items():
            if value > n:
                return key
            
        return 0
    
if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 3, 3, 4, 5, 3]
    print(s.majorityElement(nums))