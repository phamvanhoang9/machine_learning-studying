public class TrappingRainWater {
    public int trap(int[] height) {
        if (height.length == 0) {
            return 0;
        }
        int count = 0;
        int n = height.length;
        int left = 0;
        int right = n-1;
        int left_max = height[left];
        int right_max = height[right];

        while (left < right) {
            if (left_max < right_max) {
                left += 1;
                left_max = Math.max(left_max, height[left]);
                count += left_max - height[left];
            }else {
                right -= 1;
                right_max = Math.max(right_max, height[right]);
                count += right_max - height[right];
            }
        }
        return count;
    }

    public static void main(String[] args) {
        TrappingRainWater trap = new TrappingRainWater();
        int[] height = {0,1,0,2,1,0,1,3,2,1,2,1};
        System.out.println(trap.trap(height));
    }
}


