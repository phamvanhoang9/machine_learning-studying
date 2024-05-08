import java.util.Arrays;


class ProductExceptSelf {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] output = new int[n];
        for (int i = 0; i < n; i++) {
            output[i] = 1;
        }
        int left = 1;
        int right = 1;
        for (int i = 0; i < n; i++) {
            output[i] *= left;
            output[n-i-1] *= right;
            left *= nums[i];
            right *= nums[n-i-1];
        }
        return output;
    }

    public static void main(String[] args) {
        ProductExceptSelf p = new ProductExceptSelf();
        int[] nums = {1, 2, 3, 4};
        System.out.println(Arrays.toString(p.productExceptSelf(nums)));
    }
}