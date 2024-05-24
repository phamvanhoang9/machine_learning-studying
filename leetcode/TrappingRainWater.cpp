using namespace std;
#include <vector>
#include <math.h>
#include <iostream>

class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() == 0) {
            return 0;
        }

        int n = height.size();
        int count = 0;
        int left = 0;
        int right = n-1;
        int left_max = height[left];
        int right_max = height[right];

        while (left < right) {
            if (height[left] < height[right]) {
                left++;
                left_max = max(left_max, height[left]);
                count += left_max - height[left];
            } else {
                right--;
                right_max = max(right_max, height[right]);
                count += right_max - height[right];
            }
        }
        return count;
    }
};

int main() {
    Solution s;
    vector<int> height = {0,1,0,2,1,0,1,3,2,1,2,1};
    cout << s.trap(height) << endl;
}