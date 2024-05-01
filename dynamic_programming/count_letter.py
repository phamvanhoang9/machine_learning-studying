
def count_letter(string: str) -> dict:
    counter = {}
    string = string.lower()
    for letter in string:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1

    return counter

if __name__ == "__main__":
    string = "Electrical and Electronics School"
    print(count_letter(string))