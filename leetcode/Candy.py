from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        arr = [1] * len(ratings)
        for i in range(len(ratings)):
            if ratings[i] > ratings[i - 1]:
                arr[i] = arr[i - 1] + 1
            
        for i in range(len(ratings)-1, -1, -1):
            if ratings[i - 1] > ratings[i]:
                arr[i - 1] = arr[i] + 1

        return arr, sum(arr)
    
if __name__ == "__main__":
    s = Solution()
    ratings = [5, 3, 2, 6, 1, 4]
    print(s.candy(ratings)) 