class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        c = sorted(nums1 + nums2)
        n = len(c)
        if n % 2:
            return float(c[n//2])
        return (c[n//2 - 1] + c[n//2]) / 2.0