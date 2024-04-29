"""
Exercise:

Write a function called `reverse_sentence` that takes as an argument a
string that contains any number of words separated by spaces. It should return
a new string that contains the same words in reverse order. For example, if
the argument is “Reverse this sentence”, the result should be “Sentence this
reverse”.

Hint: You can use the `capitalize` methods to capitalize the first word and
convert the other words to lowercase.
"""

from typing import List


class Solution:
    def split_sentence(self, words: str) -> List[str]:
        list_words = words.split()
        return list_words
    
    def reverse_sentence(self, words: str) -> str:
        split = self.split_sentence(words)
        reversed_sentence = ' '.join(reversed(split))
        capitalized_sentence = reversed_sentence.capitalize()

        return capitalized_sentence

if __name__ == "__main__":
    s = Solution()
    words = "Hanoi University of Science and Technology"
    word2 = "Reverse this sentence"
    print(s.split_sentence(words))
    print(s.reverse_sentence(words))
    print(s.reverse_sentence(word2))
        