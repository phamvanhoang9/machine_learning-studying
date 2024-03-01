
def shift_string(S, K):
    """Given a string S of length N, shift each character of the string by K positions to the right and left, where K <= N.

    Example:
    Input: S = "abcde", K = 2
    Ouput: "cdeab", "deabc"  # Left shift and right shift respectively

    Time complexity: O(N)
    Space complexity: O(N)
    """
    N = len(S)
    K = K % N
    left_shift = S[K:] + S[:K]
    right_shift = S[-K:] + S[:-K]
    return left_shift, right_shift

# Test cases
# print(shift_string("abcde", 3)) # ('deabc', 'cdeab')


def arrange_string(S, N, M):
    """
    Given a string S, and two numbers N, M - arrange the characters of string in between the indexes N and M (both inclusive) in descending order. (Indexing starts from 0).

    Input Format:
    First line contains T - number of test cases.
    Next T lines contains a string(S) and two numbers(N, M) separated by spaces.

    Output Format:
    Print the modified string for each test case in new line.
    """
    S = list(S) # Convert string to list of characters
    S[N:M+1] = sorted(S[N:M+1], reverse=True) # Sort the characters in descending order.
    return ''.join(S)

# Test cases
# print(arrange_string("abdc", 1, 2)) # "acbd"

if __name__ == "__main__":

    print("Enter the number of test cases: ")
    
    T = int(input().strip())
    modified_strings = []

    print("Enter the string and two numbers (N, M) separated by spaces:")

    for _ in range(T):
        S, N, M = input().strip().split()
        N, M = int(N), int(M)

        modified_strings.append(arrange_string(S, N, M)) 

    print("\nModified strings: ")
    for string in modified_strings:
        print(string)