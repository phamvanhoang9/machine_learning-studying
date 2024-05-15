
def letter_map(word: str) -> dict:
    numbers = range(len(word))
    return dict(zip(word, numbers))

def shift_word(word: str, num: int) -> str:
    shifted_word = ""
    for letter in word:
        shifted_letter = chr((ord(letter) - 97 + num) % 26 + 97)
        shifted_word += shifted_letter

    return shifted_word

from collections import Counter
def counter(word: str) -> dict:
    letter_counts = Counter(word)
    return dict(letter_counts)


def most_frequent_letters(word: str) -> dict:
    mapping = counter(word)
    sorted_mapping = dict(sorted(mapping.items(), key=lambda item: item[1], reverse=True))

    return sorted_mapping

# Write the program that takes a list of words and print all the sets of words that are anagrams.
from typing import List
def sort_words(words: List[str]) -> List[str]:
    sorted_words = []
    for word in words:
        sorted_words.append("".join(sorted(word)))

    return sorted_words

def anagrams(words: List[str]) -> List[str]:
    sorted_words = sort_words(words)
    mapping = dict(zip(words, sorted_words)) # the mapping word like {'deltas': 'adelst', 'desalt': 'adelst', 'lasted': 'adelst', 'salted': 'adelst', 'slated': 'adelst', 'staled': 'adelst'}
    anagrams = {}
    for word in words:
        if mapping[word] not in anagrams:
            anagrams[mapping[word]] = [word]
        else:
            anagrams[mapping[word]].append(word)

    return anagrams

# Write a function called word_distance that takes two words with the same length and returns the number of places where two words differ.
# Hint: Using zip function to iterate two words at the same time.
def word_distance(word1: str, word2: str) -> int:
    distance = 0
    for letter1, letter2 in zip(word1, word2): # zip function will return a tuple of two words like ('h', 'w'), ('e', 'o'), ('l', 'r'), ('l', 'l'), ('o', 'd')
        if letter1 != letter2:
            distance += 1

    return distance

# Write a program that finds all of the metathesis pairs in the word list
# Hint: The words in the metathesis pair must be anagrams of each other.
def metathesis_pairs(words: List[str]) -> List[str]:
    anagram_mapping = anagrams(words)
    metathesis_pairs = []
    for key, value in anagram_mapping.items():
        if len(value) > 1:
            for i in range(len(value)):
                for j in range(i+1, len(value)):
                    if word_distance(value[i], value[j]) == 2:
                        metathesis_pairs.append((value[i], value[j]))

    return metathesis_pairs

# main
print(metathesis_pairs(["converse", "conserve", "hello", "world"]))