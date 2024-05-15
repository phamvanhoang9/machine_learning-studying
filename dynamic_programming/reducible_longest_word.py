
def load_words(file_path):
    with open(file_path, 'r') as f:
        # using set() to avoid duplicates
        words = set(word.strip().lower() for word in f.readlines()) 
    # adding `i` and `a` to the set because they are valid words
    words.update(['i', 'a'])
    return words

def generate_children(word):
    """Generate all possible children of the word by removing one letlter."""
    children = []
    for i in range(len(word)):
        children.append(word[:i] + word[i+1:])
    
    return children

def is_reducible(word, word_set, memo):
    """Check if a word is reducible."""
    if word in memo:
        return memo[word]
    if word in word_set:
        if word in ('i', 'a', ''):
            memo[word] = True
            return True
        for child in generate_children(word):
            if child in word_set and is_reducible(child, word_set, memo):
                memo[word] = True
                return True
            
        memo[word] = False
        return False

def find_longest_reducible_word(word_set):
    memo = {}
    longest_word = ""
    for word in word_set:
        if is_reducible(word, word_set, memo):
            if len(word) > len(longest_word):
                longest_word = word

    return longest_word
