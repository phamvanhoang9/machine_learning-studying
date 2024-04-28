import java.util.ArrayList;
import java.util.Arrays;


public class MergeSort {
    public static int[] merge(int[] leftArray, int[] rightArray) {
        ArrayList<Integer> resultArray = new ArrayList<>();
        int leftIdx = 0;
        int rightIdx = 0;
        
        while (leftIdx < leftArray.length && rightIdx < rightArray.length) {
            if (leftArray[leftIdx] > rightArray[rightIdx]) {
                resultArray.add(rightArray[rightIdx]);
                rightIdx++;
            } else {
                resultArray.add(leftArray[leftIdx]);
                leftIdx++;
            }
        }
        
        while (leftIdx < leftArray.length) {
            resultArray.add(leftArray[leftIdx]);
            leftIdx++;
        }

        while (rightIdx < rightArray.length) {
            resultArray.add(rightArray[rightIdx]);
            rightIdx++;
        }

        return resultArray.stream().mapToInt(i->i).toArray();
    }

    public int[] mergeSort(int[] array) {
        if (array.length < 2) {
            return array;
        }

        final int MIDDLE = array.length / 2;
        final int[] LEFT_ARRAY = Arrays.copyOfRange(array, 0, MIDDLE);
        final int[] RIGHT_ARRAY = Arrays.copyOfRange(array, MIDDLE, array.length);

        return merge(mergeSort(LEFT_ARRAY), mergeSort(RIGHT_ARRAY));
    }

    public static void main(String[] args) {
        MergeSort s = new MergeSort();
        int[] array = {5, 4, 6, 8, 7, 3, 2, 9, 1};
        int[] sortedArray = s.mergeSort(array);
        System.out.println("Sorted Array: " + Arrays.toString(sortedArray));
    }
}
