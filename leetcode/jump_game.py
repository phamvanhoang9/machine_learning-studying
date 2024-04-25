from typing import List 


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         max_jump_idx = len(nums) - 1
#         i = 1
#         while (i < len(nums)-1):
#             idx = nums[i]
#             if idx == 0:
#                 return False
#             step = i + idx
#             if (step == max_jump_idx):
#                 return True
#             elif (step < max_jump_idx):
#                 i = step 
        
#         return False
    
if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    # nums = [3, 2, 1, 0, 4]
    print(s.canJump(nums))
            