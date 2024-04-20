public class RemoveDuplicatesII {
    public int removeDuplicates(int[] nums) {
        int k = 2;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[k-2]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
    public static void main(String[] args) {
        RemoveDuplicatesII re = new RemoveDuplicatesII();
        int[] nums = {1, 2, 2, 2, 3, 3, 3, 3, 6, 7, 7, 7, 8, 8, 9};
        System.out.println(re.removeDuplicates(nums));
    }
}
