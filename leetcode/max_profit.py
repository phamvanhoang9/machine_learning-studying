from typing import List
import time

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         profits = []
#         for k in range(0, len(prices)-1):
#             for n in range(k+1, len(prices)-1):
#                 if (prices[n] > prices[k]):
#                     price = prices[n] - prices[k]
#                     profits.append(price)
        
#         max_profit = max(profits) if profits else 0

#         return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit
    
if __name__ == "__main__":
    s = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    # prices = [7, 6, 4, 3, 1]
    start = time.time()
    print(s.maxProfit(prices))
    end = time.time()

    print("Duration: ", (end - start)*1_000_000)