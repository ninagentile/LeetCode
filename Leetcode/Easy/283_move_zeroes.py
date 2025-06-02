class Solution(object):
    def moveZeroes(self, nums: list[int]):
        """
        283. Move Zeroes
        Given an integer array nums, move all 0's to the end of it while
        maintaining the relative order of the non-zero elements.

        Note that you must do this in-place without making a copy of the
        array.

        Parameters
        ----------
        :type nums: List[int]

        Returns
        -------
        :rtype: None Do not return anything, modify nums in-place
        instead.
        """
        curr_idx = 0
        last_non_zero_idx = 1
        if len(nums) == 1:
            return
        while (last_non_zero_idx < len(nums)) and (curr_idx < len(nums)):
            # If the element at last_non_zero_idx is a 0, increment
            # last_non_zero_idx
            if nums[last_non_zero_idx] == 0:
                last_non_zero_idx += 1
            else:
                # If the current element is a zero, we swap it with the
                # element at last_non_zero_idx
                if nums[curr_idx] == 0:
                    # Swap the number only if the last_non_zero_idx is
                    # greater than curr_idx (to avoid moving a 0 toward
                    # the front of the array)
                    if last_non_zero_idx < curr_idx:
                        last_non_zero_idx += 1
                        continue
                    nums[curr_idx] = nums[last_non_zero_idx]
                    nums[last_non_zero_idx] = 0
                    last_non_zero_idx += 1
                curr_idx += 1
