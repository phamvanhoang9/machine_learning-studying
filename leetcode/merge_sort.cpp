using namespace std;
#include <iostream>
#include <vector>


class Solution {
private: 
    vector<int> merge(vector<int> leftArray, vector<int> rightArray) {
        vector<int> resultArray;
        int leftIdx = 0;
        int rightIdx = 0;

        while (leftIdx < leftArray.size() && rightIdx < rightArray.size()) {
            if (leftArray[leftIdx] > rightArray[rightIdx]) {
                resultArray.push_back(rightArray[rightIdx++]);
            } else {
                resultArray.push_back(leftArray[leftIdx++]);
            }
        }

        while (leftIdx < leftArray.size()) {
            resultArray.push_back(leftArray[leftIdx++]);
        }

        while (rightIdx < rightArray.size()) {
            resultArray.push_back(rightArray[rightIdx++]);
        }

        return resultArray;
    }

public:
    vector<int> mergeSort(vector<int> array) {
        if (array.size() < 2) {
            return array;
        }

        const int MIDDLE = array.size() / 2;
        vector<int> leftArray(array.begin(), array.begin() + MIDDLE);
        vector<int> rightArray(array.begin() + MIDDLE, array.end());

        return merge(mergeSort(leftArray), mergeSort(rightArray));
    }
};

int main() {
    Solution s;
    vector<int> array = {5, 7, 6, 9, 8, 3, 2, 1, 4};
    vector<int> sortedArray = s.mergeSort(array);
    
    for (int i : sortedArray) {
        cout << i << " ";
    }
    cout << endl;

    return 0;
}