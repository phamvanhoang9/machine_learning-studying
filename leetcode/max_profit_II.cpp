using namespace std;
#include <iostream>
#include <vector>


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profitFromPriceGain = 0;
        for (int i = 0; i < prices.size()-1; i++) {
            if (prices[i] < prices[i+1]) {
                profitFromPriceGain += prices[i+1] - prices[i];
            }
        }
        return profitFromPriceGain;
    }
};

int main() {
    Solution s;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    cout << s.maxProfit(prices) << endl;
}