public class JumpGame2 {
    public int jump(int[] nums) {
        int jumps = 0, currEnd = 0, currFarthest = 0;
        for (int i = 0; i < nums.length - 1; i++) {
            currFarthest = Math.max(currFarthest, i + nums[i]);
            if (i == currEnd) {
                jumps++;
                currEnd = currFarthest;
            }
        }

        return jumps;
    }

    public static void main(String[] args) {
        JumpGame2 j = new JumpGame2();
        int[] nums = {2, 3, 1, 1, 4};
        System.out.println(j.jump(nums));
    }
}
