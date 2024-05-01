from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        return sum(i < j for i, j in enumerate(sorted(citations, reverse=True)))

if __name__ == "__main__":
    s = Solution()
    citations = [3, 0, 6, 1, 5]
    citations2 = [1,3,1]
    print(s.hIndex(citations=citations))