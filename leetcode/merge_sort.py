class Solution:
    def merge(self, left_arr, right_arr):
        result_arr = []
        left_idx = 0
        right_idx = 0

        while (left_idx < len(left_arr) and right_idx < len(right_arr)):
            if (left_arr[left_idx] > right_arr[right_idx]):
                result_arr.append(right_arr[right_idx])
                right_idx += 1
            else:
                result_arr.append(left_arr[left_idx])
                left_idx += 1

        return result_arr + left_arr[left_idx:] + right_arr[right_idx:]
    
    def merge_sort(self, arr):
        if (len(arr) < 2):
            return arr
        
        MIDDLE_INDEX = len(arr) // 2
        LEFT_ARRAY = arr[:MIDDLE_INDEX]
        RIGHT_ARRAY = arr[MIDDLE_INDEX:]

        return self.merge(self.merge_sort(LEFT_ARRAY), self.merge_sort(RIGHT_ARRAY))
    
if __name__ == "__main__":
    s = Solution()
    array = [4, 5, 3, 2, 9, 7, 8, 1, 6]
    print(s.merge_sort(array))