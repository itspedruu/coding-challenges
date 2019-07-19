from math import ceil

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        pair = (len(nums1) + len(nums2)) % 2 == 0
        startIndex = ceil((len(nums1) + len(nums2)) / 2) - 1
        sortedArray = sorted(nums1 + nums2)
        return (sortedArray[startIndex] + sortedArray[startIndex + 1]) / 2 if pair else float(sortedArray[startIndex])

median = Solution().findMedianSortedArrays([], [2,3])
print('The median is {}'.format(median))