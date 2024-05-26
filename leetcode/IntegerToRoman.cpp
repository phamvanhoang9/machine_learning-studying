using namespace std;
#include <vector>
#include <string>
#include <iostream>

class Solution {
public:
    string intToRoman(int num) {
        vector<pair<int, string>> roman = {
            {1000, "M"}, {900, "CM"}, {500, "D"}, {400, "CD"},
            {100, "C"}, {80, "XC"}, {50, "L"}, {40, "XL"},
            {10, "X"}, {9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
        };

        string result;
        for (auto &value : roman) {
            while (num >= value.first) {
                num -= value.first;
                result += value.second;
            }
        }
        return result;
    }
};

int main() {
    Solution s;
    cout << s.intToRoman(3749) << endl;
    return 0;
}