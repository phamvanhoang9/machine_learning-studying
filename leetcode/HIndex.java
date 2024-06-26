import java.util.Arrays;


public class HIndex {
    public int hIndex(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int hIndex = 0;
        for (int i = 0; i < n; i++) {
            int h = Math.min(citations[i], n - i);
            hIndex = Math.max(hIndex, h);
        }
        return hIndex;
    }

    public static void main(String[] args) {
        HIndex hIndex = new HIndex();
        int[] citations = {3, 0, 6, 1, 5};
        System.out.println(hIndex.hIndex(citations));
    }
}