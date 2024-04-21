using namespace std;
#include <vector>
#include <iostream>
#include <unordered_map>



class Solution {
public: 
    int majorityElement(vector<int>& nums) {
        // "&" is used to pass the vector "nums" by reference to the function
        int n = nums.size();
        unordered_map<int, int> m; 

        for (int i = 0; i < n; i++) {
            m[nums[i]]++;
        }

        n = n/2;
        for (auto x : m) {
            if (x.second > n) {
                return x.first;
            }
        }

        return 0;
    }
};

int main() {
    Solution s;
    vector<int> nums = {2, 3, 3, 3, 4, 5, 3};
    cout << s.majorityElement(nums) << endl;
}