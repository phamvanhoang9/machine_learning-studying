
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list_of_string = s.strip().split()

        if len(list_of_string) == 1:
            return len(list_of_string[0])
        
        return len(list_of_string[-1])

if __name__ == "__main__":
    s = Solution()
    str = "Pham Van Hoang"
    print(s.lengthOfLastWord(str))