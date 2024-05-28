public class LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        s = s.trim(); // ~strip() in python
        String[] words = s.split(" "); // List of words

        if (words.length == 1) {
            return words[0].length();
        }
        return words[words.length - 1].length();
    }

    public static void main(String[] args) {
        LengthOfLastWord len = new LengthOfLastWord();
        String str = "Hello, World!";
        System.out.println(len.lengthOfLastWord(str));
    }
}

