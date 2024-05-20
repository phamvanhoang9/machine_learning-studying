using namespace std;
#include <vector>
#include <numeric>


class Solution{
public:
    int candy(vector<int>& ratings) {
        vector<int> arr(ratings.size(), 1);

        for (int i = 0; i < ratings.size(); i++) {
            if (ratings[i] > ratings[i - 1]) {
                arr[i] = arr[i - 1] + 1;
            }
        }
        for (int i = ratings.size() - 1; i > -1; i--) {
            if (ratings[i - 1] > ratings[i]) {
                arr[i - 1] = arr[i] + 1;
            }
        }
        return accumulate(arr.begin(), arr.end(), 0);
    }
};