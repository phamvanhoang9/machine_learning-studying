using namespace std;
#include <iostream>
#include <vector>


class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int k = 2;
        for (int j = 2; j < nums.size(); j++) {
            if (nums[j] != nums[k-2]) {
                nums[k] = nums[j];
                k++;
            }
        }
        return k;
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 1, 1, 1, 2, 2, 2, 4, 4, 6, 7, 7, 7};
    cout << s.removeDuplicates(nums) << endl;
}