
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


# main
word = "stevehoangphamvanhoang"
mapping = counter(word=word)
print(mapping)
print(most_frequent_letters(word=word))