public class MaxProfitII {
    public int maxProfit(int[] prices) {
        int profitFromPriceGain = 0;
        
        for (int i = 0; i < prices.length-1; i++) {
            if (prices[i] < prices[i+1]) {
                profitFromPriceGain += prices[i+1] - prices[i];
            }
        }
        return profitFromPriceGain;
    }
    
    public static void main(String[] args) {
        MaxProfitII profit = new MaxProfitII();
        int[] prices = {7, 1, 5, 3, 6, 4};
        System.out.println(profit.maxProfit(prices));
    }
}
