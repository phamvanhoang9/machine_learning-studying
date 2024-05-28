using namespace std;
#include <iostream>
#include <vector>

class Solution {
public:
    int lengthOfLastWord(string s) {
        int length = 0;
        bool counting = false;

        for (int i = s.length() - 1; i >= 0; i--) {
            if (s[i] != ' ') {
                counting = true;
                length++;
            }
            else if (counting) {
                break;
            }
        }
        return length;
    }
};

int main() {
    Solution s;
    string str = "Hello, World!   ";
    cout << s.lengthOfLastWord(str) << endl;
}