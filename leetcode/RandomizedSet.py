import random


class RandomizedSet:
    """ 
    Time complexity must be O(1) for insert, remove and getRandom
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.data_dict = {}
        

    def insert(self, val: int) -> list|dict:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data_dict:
            return False
        self.data.append(val)
        self.data_dict[val] = len(self.data) - 1
        return self.data, self.data_dict
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data_dict:
            return False
        idx = self.data_dict[val] # get the index of the value to be removed
        last_val = self.data[-1] # get the last value in the list
        self.data[idx] = last_val # replace the value to be removed with the last value
        self.data_dict[last_val] = idx # update the index of the last value
        self.data.pop() # remove the last value
        del self.data_dict[val] # remove the value from the dictionary
        return self.data, self.data_dict
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.data)
    

if __name__ == "__main__":
    randomizedSet = RandomizedSet()
    print(randomizedSet.insert(1))
    print(randomizedSet.insert(3))
    print(randomizedSet.insert(2))
    print(randomizedSet.remove(3))
    print(randomizedSet.getRandom())
