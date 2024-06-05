from typing import List


class Solution:
    def fullJustify(self, words: List[int], maxWidth: int) -> List[str]:
        # Firstly, we initialize some variables:
        # res is used to store the rest of words after justification
        # line is used to count the number of word in each line
        # width is used to count the lenght of sentence
        res, line, width = [], [], 0

        for w in words:
            # Check if adding next word would be exceeded
            if width + len(line) + len(w) > maxWidth:
                for i in range(maxWidth - width):
                    # You can imagine that a line will have a space between two words ' '
                    # If the line has n words that will have n-1 space 
                    line[i % (len(line) - 1 or 1)] += ' ' # or 1 if the line has only one word
                res, line, width = res + [''.join(line)], [], 0 # after the loop, we reset the line and the width to do for next line

            line += [w]
            width += len(w)

        return res + [' '.join(line).ljust(maxWidth)] # Eventually, if the last line doesn't have enough word to fill full maxWidth, it should be added the extra space from the left to the right.

if __name__ == "__main__":
    s = Solution()
    words = ["My", "name", "is", "Steve", "Hoang.", "I", "am", "study", "at", "HUST."]
    maxWidth = 16
    result = s.fullJustify(words, maxWidth)

    for line in result:
        print(f"'{line}'")