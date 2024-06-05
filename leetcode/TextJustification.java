import java.util.ArrayList;
import java.util.List;


public class TextJustification {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> res = new ArrayList<>(); // we need an array to store the result
        List<String> line = new ArrayList<>(); // we need an other to count number of words in a line
        int width = 0; // current width

        for (String w : words) {
            if (width + line.size() + w.length() > maxWidth) {
                for (int i = 0; i < maxWidth - width; i++) {
                    // You can imagine that a line will have a space between two words ' '
                    // If the line has n words that will have n-1 space
                    line.set(i % (line.size() - 1 == 0 ? 1 : line.size() - 1),
                            line.get(i % (line.size() - 1 == 0 ? 1 : line.size() - 1)) + " ");
                }
                res.add(String.join("", line));
                line.clear();
                width = 0;
            }
            line.add(w);
            width += w.length();
        }
        res.add(String.join(" ", line).trim() + " ".repeat(maxWidth - String.join(" ", line).length()));
        return res;
    }

    public static void main(String[] args) {
        TextJustification textJustification = new TextJustification();
        String[] words = {"This", "is", "an", "example", "of", "text", "justification."};
        int maxWidth = 16;
        List<String> justifiedText = textJustification.fullJustify(words, maxWidth);

        for (String line : justifiedText) {
            System.out.println(line);
        }
    }
}
