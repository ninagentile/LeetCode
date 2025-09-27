import numpy as np


class Solution:
    def merge(
        self, nums1: list[int], m: int, nums2: list[int], n: int
    ) -> None:
        """
        88. Merge Sorted Array

        You are given two integer arrays nums1 and nums2, sorted in
        non-decreasing order, and two integers m and n, representing
        the number of elements in nums1 and nums2 respectively.

        Merge nums1 and nums2 into a single array sorted in
        non-decreasing order.

        The final sorted array should not be returned by the function,
        but instead be stored inside the array nums1. To accommodate
        this, nums1 has a length of m + n, where the first m elements
        denote the elements that should be merged, and the last n
        elements are set to 0 and should be ignored. nums2 has a length
        of n.
        """
        # Initialize three pointers: one for nums1, one for nums2, and
        # one for the current position starting from the end of the
        # array nums1
        p1 = m - 1
        p2 = n - 1
        p_curr = m + n - 1

        while p_curr != -1:
            # Get the current element from nums1
            if p1 < 0:
                el1 = -np.inf
            else:
                el1 = nums1[p1]

            # Get the current element from nums2
            if p2 < 0:
                el2 = -np.inf
            else:
                el2 = nums2[p2]
            # Compare the elements, write at position p_curr the
            # highest element and update the corresponding pointer
            if el1 > el2:
                nums1[p_curr] = el1
                p1 -= 1
            else:
                nums1[p_curr] = el2
                p2 -= 1

            p_curr -= 1
