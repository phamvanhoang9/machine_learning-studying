class Solution:
    def merge(self, nums1, m, nums2, n):
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()
        return nums1

# Time: O(nlogn)
# Space: O(1)

if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    s = Solution()
    print(s.merge(nums1, m, nums2, n)) 