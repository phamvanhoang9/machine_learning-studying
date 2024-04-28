using namespace std;
#include <iostream>
#include <vector>


class Solution {
public: 
    int jump(vector<int>& nums) {
        int jumps = 0, currEnd = 0, currFarthest = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            currFarthest = max(currFarthest, i + nums[i]);
            if (i == currEnd) {
                jumps++;
                currEnd = currFarthest;
            }
        }
        return jumps;
    }
};

int main() {
    Solution s;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << s.jump(nums) << endl;
}