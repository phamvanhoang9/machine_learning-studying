public class RemoveElement {
    public int removeElement(int [] nums, int val) {
        int index = 0;

        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                nums[index] = nums[i];
                index += 1;
            }
        }

        return index;
    }
    
    public static void main(String[] args) {
        RemoveElement re = new RemoveElement();
        int [] nums = {3, 2, 2, 3, 7, 8};
        int val = 3;
        int result = re.removeElement(nums, val);
        System.out.println(result);
    }
}

