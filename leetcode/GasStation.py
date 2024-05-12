from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if (sum(gas) < sum(cost)):
            return -1
        
        start_index = 0
        gas_tank = 0
        
        for i in range(len(gas)):
            gas_tank += gas[i] - cost[i]

            if gas_tank < 0:
                gas_tank = 0
                start_index += 1

        return start_index
    
if __name__ == "__main__":
    s = Solution()
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print(s.canCompleteCircuit(gas, cost))