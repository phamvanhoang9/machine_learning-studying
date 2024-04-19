using namespace std;
#include <iostream>
#include <vector>


class Solution {
public: 
    int removeDuplicates(vector<int>&nums) {
        int k = 1;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] != nums[i-1]) {
                nums[k] = nums[i];
                k++;
            }
        }
        return k;
    }
};

int main() {
    Solution s;
    vector<int> nums = {1, 1, 1, 3, 4, 6, 6, 7, 7};
    cout << s.removeDuplicates(nums) << endl;
}