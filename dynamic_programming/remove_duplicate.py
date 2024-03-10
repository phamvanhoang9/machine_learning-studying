"""
Given a string str which may contains lowercase and uppercase chracters. 
The task is to remove all duplicate characters from the string and find the resultant string. 
The order of remaining characters in the output should be same as in the original string.

Your Task:
Complete the function removeDuplicates() which takes a string str, as input parameters and returns a string denoting the answer. You don't have to print answer or take inputs.

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
"""

def removeDuplicates(s):
    n = len(s)
    ans = []
    seen = set() # To keep track of the characters that have been seen
    for i in range(n):
        if s[i] not in seen:
            seen.add(s[i])
            ans.append(s[i])
    return ''.join(ans)

# Example
s = "PHamVanhoang"
print(removeDuplicates(s)) # Output: PHamVnog