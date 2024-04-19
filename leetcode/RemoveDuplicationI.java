public class RemoveDuplicationI {
    public int removeDuplicates(int[] nums) {
        int k = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[i-1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
    public static void main(String[] args) {
        RemoveDuplicationI re = new RemoveDuplicationI();
        int[] nums = {2, 3, 3, 3, 5, 6, 6, 7};
        System.out.println(re.removeDuplicates(nums));
    }
}


