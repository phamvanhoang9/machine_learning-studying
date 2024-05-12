public class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (getSum(gas) < getSum(cost)) {
            return -1;
        }

        int start_idx = 0;
        int gas_tank = 0;

        for (int i = 0; i < gas.length; i++) {
            gas_tank += gas[i] - cost[i];

            if (gas_tank < 0) {
                gas_tank = 0;
                start_idx = i + 1;
            }
        }

        return start_idx;
    }

    private int getSum(int[] arr) {
        int sum = 0;
        for (int val : arr) {
            sum += val;
        }
        return sum;
    }
}

