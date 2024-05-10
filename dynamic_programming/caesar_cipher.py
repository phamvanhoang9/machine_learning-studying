"""
Applying Caesar cipher to shift any word.
"""

def letter_map(word: str) -> dict:
    numbers = range(len(word))
    return dict(zip(word, numbers))

def shift_word(word: str, num: int) -> str:
    shifted_word = ""
    for letter in word:
        shifted_letter = chr((ord(letter) - 97 + num) % 26 + 97)
        shifted_word += shifted_letter

    return shifted_word


word = "abc"
mapping = letter_map(word)
print(mapping)
print(shift_word(word, 2))
