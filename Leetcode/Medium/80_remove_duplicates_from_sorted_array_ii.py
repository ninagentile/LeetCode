class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        """
        80. Remove Duplicates from Sorted Array II
        Given an integer array nums sorted in non-decreasing order,
        remove some duplicates in-place such that each unique element
        appears at most twice. The relative order of the elements should
        be kept the same.

        Since it is impossible to change the length of the array in some
        languages, you must instead have the result be placed in the
        first part of the array nums. More formally, if there are k
        elements after removing the duplicates, then the first k
        elements of nums should hold the final result. It does not
        matter what you leave beyond the first k elements.

        Return k after placing the final result in the first k slots of
        nums.

        Do not allocate extra space for another array. You must do this
        by modifying the input array in-place with O(1) extra memory.
        """
        p_curr = 0
        p_next = 0
        while p_curr < len(nums):
            # Stop condition when p_next reaches the end of the array.
            if p_next >= len(nums):
                return p_curr
            # Get the current element
            curr_elem = nums[p_next]
            # Compare the current element with 2 elements before, if it
            # is different, write it at the current index p_curr and
            # update p_curr
            if (p_curr - 2 < 0) or (curr_elem != nums[p_curr - 2]):
                nums[p_curr] = curr_elem
                p_curr += 1
            # Otherwise, just update the p_next index
            p_next += 1
