using namespace std;
#include <iostream>
#include <vector>
#include <algorithm>


class Solution {
public: 
    int hIndex(vector<int>& citations) {
        sort(citations.begin(), citations.end());
        int n = citations.size();
        int hIndex = 0;
        for (int i = 0; i < n; i++) {
            int h = min(citations[i], n - i);
            hIndex = max(hIndex, h);
        }
        return hIndex;
    }
};

int main() {
    Solution s;
    vector<int> citations = {3, 0, 6, 1, 5};
    cout << s.hIndex(citations) << endl;
}