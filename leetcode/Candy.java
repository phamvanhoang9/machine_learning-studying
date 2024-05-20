import java.util.Arrays;


class Candy {
    public int candy(int[] ratings) {
        int[] arr = new int[ratings.length];
        Arrays.fill(arr, 1);

        for (int i =  0; i < ratings.length; i++) {
            if (ratings[i] > ratings[i - 1]) {
                arr[i] = arr[i - 1];
            }
        }
        for (int i = ratings.length - 1; i > -1; i--) {
            if (ratings[i-1] > ratings[i]) {
                arr[i - 1] = arr[i] + 1;
            }
        }
        return Arrays.stream(arr).sum();
    }
}