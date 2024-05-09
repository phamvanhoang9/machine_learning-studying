using namespace std;
#include <stdlib.h> // for rand()
#include <time.h>
#include <vector>
#include <unordered_map>


class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        srand(time(NULL)); // seed the random number generator
    }
    
    vector<int> v;
    unordered_map<int, int> m;
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        auto it = m.find(val);
        if(it != m.end()) return false;
        v.push_back(val);
        m[val] = v.size()-1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        auto it = m.find(val);
        if(it == m.end()) return false;
        int idx = it->second; // index of val in v
        m[v.back()] = idx; // v.back() is the last element in v
        swap(v[idx], v.back());
        v.pop_back();
        m.erase(it);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return v[rand()%v.size()]; // using % to get a random index in v
    }
};

int main() {
    RandomizedSet* obj = new RandomizedSet(); // create a new object
    bool param_1 = obj->insert(1); // insert 1
    bool param_2 = obj->remove(2); // remove 2
    int param_3 = obj->getRandom(); // get a random element
    return 0; // return 0
}