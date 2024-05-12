using namespace std;
#include <vector>
#include <numeric>

class Solution {
public: 
    int canCompleteCircuit(vector<int> gas, vector<int> cost) {
        if (accumulate(gas.begin(), gas.end(), 0) < accumulate(cost.begin(), cost.end(), 0)) {
            return -1;
        }

        int start_idx = 0;
        int gas_tank = 0;

        for (int i = 0; i < gas.size(); i++) {
            gas_tank += gas[i] + cost[i];
            
            if (gas_tank < 0) {
                gas_tank = 0;
                start_idx = i + 1;
            }
        }
        return start_idx;
    }
};