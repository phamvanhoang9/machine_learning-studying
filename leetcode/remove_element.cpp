using namespace std;
#include <iostream>
#include <vector>

class Solution {
public: 
    int removeElement(vector<int>&nums, int val) {
        int index = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] != val) {
                nums[index] = nums[i];
                index += 1;
            }
        }
        return index;
    }
};

int main() {
    Solution s;
    vector<int> nums = {3, 2, 2, 3, 5, 7};
    int val = 3;
    cout << s.removeElement(nums, val) << endl;
}