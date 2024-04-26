using namespace std;
#include <iostream>
#include <vector>


class Solution {
public: 
    bool canJump(vector<int>& nums) {
        int goal = nums.size() - 1;
        for (int i = goal; i >= 0; i--) {
            if (i + nums[i] >= goal) {
                goal = i;
            }
        }
        return goal == 0;
    }
};

int main() {
    Solution s;
    vector<int> nums = {2, 3, 1, 1, 4};
    cout << s.canJump(nums) << endl;
}