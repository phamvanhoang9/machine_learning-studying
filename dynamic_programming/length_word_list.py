"""
Exercise:

Write a function called total_length that takes a list of strings and
returns the total length of the strings. The total length of the words in
word_list should be 902, 728.
"""

from typing import List


class Solution:
    def calc(self, string: str) -> int:
        return len(string.split())
    
    def total_length(self, strings: List[str]) -> int:
        sum_length = 0
        for string in strings:
            sum_length += self.calc(string)
        
        return sum_length

if __name__ == "__main__":
    s = Solution()
    print(s.calc("My name is Steve"))
    strings = ["My name is Steve", "I am a student of Hanoi University of Science and Technology"]
    print(s.total_length(strings))