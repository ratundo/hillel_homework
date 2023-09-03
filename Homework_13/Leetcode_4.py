# https://leetcode.com/problems/median-of-two-sorted-arrays
# 4. Median of Two Sorted Arrays
# Hard
# Companies

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

import numpy as np
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return np.median(sorted(nums1 + nums2))