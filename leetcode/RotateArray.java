import java.util.Arrays;



public class RotateArray {
    public static int[] reverse(int[] nums) {
        int i = 0;
        int end = nums.length - 1;

        while (i < end) {
            int temp = nums[i];
            nums[i] = nums[end];
            nums[end] = temp;
            i++;
        }
        return nums;
    }
    
    public int[] rotate(int[] nums, int k) {
        for (int i = 0; i < k; i++) {
            reverse(nums);
        }
        return nums;
    }
    
    public static void main(String[] args) {
        RotateArray ro = new RotateArray();
        int[] nums = {1, 2, 3, 4, 5};
        int k = 3;
        System.out.println(Arrays.toString(ro.rotate(nums, k)));
    }
}
