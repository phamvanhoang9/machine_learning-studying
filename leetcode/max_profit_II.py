from typing import List 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_from_price_gain = 0
        for idx in range(len(prices) - 1):
            if prices[idx] < prices[idx + 1]:
                profit_from_price_gain += (prices[idx + 1] - prices[idx])
        return profit_from_price_gain
    
if __name__ == "__main__":
    s = Solution()  
    # prices = [7, 1, 5, 3, 6, 4]
    # prices = [1,2,3,4,5]
    prices = [7,6,4,3,1]
    print(s.maxProfit(prices))

