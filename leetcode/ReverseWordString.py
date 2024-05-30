class Solution:
    def reverseWord(self, s:str) -> str:
        res = []
        temp = ""
        for c in s:
            if c != " ":
                temp += c
            elif temp != "":
                res.append(temp)
                temp = ""
        if temp != "":
            res.append(temp)

        return " ".join(res[::-1])
    
if __name__ == "__main__":
    s = Solution()
    str = "My   name is   Hoang  "
    print(s.reverseWord(str))