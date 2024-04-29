"""
Exercise:

A palindrome is a word that is spelled the same backward and forward, like
“noon” and “rotator”. Write a function called `is_palindrome` that takes a
string argument and returns True if it is a palindrome and False otherwise.

You can use the following loop to find all of the palindromes in the word list
with at least 3 letters.
"""

from typing import List 


class Solution:
    def is_palindrome(self, word: str) -> bool:
        if (word == ''.join(reversed(word))):
            return True
        
        return False
    
    def find_palindrome(self, words: List[str]) -> List[str]:
        checked_words = []
        for word in words:
            if len(word) >= 3 and self.is_palindrome(word):
                checked_words.append(word)

        return checked_words

    
if __name__ == "__main__":
    s = Solution()

    print(s.is_palindrome("noon"))
    print(s.is_palindrome("hat"))

    words = ["noon", "rotator", "hat"]
    print(f"The list of palindromes are: {s.find_palindrome(words=words)}")