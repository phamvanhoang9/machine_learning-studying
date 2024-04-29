"""
Exercise:

Two words are `anagrams` if you can rearrange the letters from one to spell the
other. For example, `tops` is an anagram of `stop`.
One way to check whether two words are anagrams is to sort the letters in
both words. If the lists of sorted letters are the same, the words are anagrams.
Write a function called `is_anagram` that takes two strings and returns
`True` if they are anagrams.
Using your function and the word list, find all the anagrams of `takes`.
"""

from typing import List

class Solution:
    # Check if 2 words are anagram
    def is_anagram(self, word1: str, word2: str) -> bool:
        word1 = sorted(word1)
        word2 = sorted(word2)
        if (word1 == word2):
            return True
        
        return False
    
    # Find all anagrams with the reference word
    def find_anagrams(self, list_words: List[str], ref_word: str) -> List[str]:
        list_anagrams = []
        for word in list_words:
            if self.is_anagram(word, ref_word):
                list_anagrams.append(word)

        return list_anagrams
    
if __name__ == "__main__":
    s = Solution()
    print(s.is_anagram("tops", "stop"))
    print(s.is_anagram("leran", "study"))
    
    list_words = ["takes", "stalk", "ktaes", "teaks", "lack"]
    ref_word = "takes"

    print(f"The list of anagrams of `takes` are: {s.find_anagrams(list_words, ref_word)}")
        