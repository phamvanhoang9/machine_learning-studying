using namespace std;
#include <vector>
#include <iostream>


class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result(nums.size(), 1);
        int left = 1;
        int right = 1;
        for (int i = 0; i < nums.size(); i++) {
            result[i] *= left;
            left *= nums[i];
            result[nums.size() - 1 - i] *= right;
            right *= nums[nums.size() - 1 - i];
        }
        return result;
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 2, 3, 4};
    vector<int> result = s.productExceptSelf(nums);
    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    return 0;
}