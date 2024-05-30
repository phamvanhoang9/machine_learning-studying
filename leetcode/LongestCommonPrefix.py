from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs = sorted(strs)

        lcp = ""
        fist_word = strs[0]
        last_word = strs[-1]

        for i in range(min(len(fist_word), len(last_word))):
            if (fist_word[i] == last_word[i]):
                lcp += fist_word[i]
            else:
                break

        return lcp
    
if __name__ == "__main__":
    s = Solution()
    strs = ["flower","flow","flight"]
    strs2 = ["dog","racecar","car"]
    print(s.longestCommonPrefix(strs2))