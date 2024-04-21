import java.util.HashMap;
import java.util.Map;



public class MajorityElement {
    public int majorityElement(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < n; i++) {
            map.put(nums[i],  map.getOrDefault(nums[i], 0) + 1);
        }

        n = n / 2;
        for (Map.Entry<Integer, Integer> entry: map.entrySet()) {
            if (entry.getValue() > n) {
                return entry.getKey();
            }
        }
        return 0;
    }

    public static void main(String[] args) {
        MajorityElement m = new MajorityElement();
        int[] nums = {2, 3, 3, 3, 4, 5, 3};
        System.out.println(m.majorityElement(nums));
    }
}
