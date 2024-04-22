using namespace std;
#include <iostream>
#include <vector>


class Solution {
public: 
    void reverse(vector<int>::iterator start, vector<int>::iterator end) {
        while (start < end) {
            int temp = *start;
            *start = *end;
            *end = temp;
            start++;
            end--;
        }
    }

    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;

        reverse(nums.begin(), nums.end()); // reverse the whole array
        reverse(nums.begin(), nums.begin() + k); // reverse the first k elements
        reverse(nums.begin() + k, nums.end()); // reverse the last k elements
    }
};

int main() {
    Solution so;
    vector<int> nums = {1, 2, 3, 4, 5};
    int k = 3;

    so.rotate(nums, k);

    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}