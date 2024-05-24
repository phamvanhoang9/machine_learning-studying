from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left, right = 0, n-1
        left_max, right_max = height[left], height[right]
        count = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                count += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                count += right_max - height[right] 

        return count
       
if __name__ == "__main__":
    s = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(s.trap(height=height))