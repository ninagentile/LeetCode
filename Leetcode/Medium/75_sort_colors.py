class Solution(object):
    def sort_colors(self, nums: list[int]):
        """
        75. Sort Colors
        Given an array nums with n objects colored red, white, or blue,
        sort them in-place so that objects of the same color are
        adjacent, with the colors in the order red, white, and blue.

        We will use the integers 0, 1, and 2 to represent the color red,
        white, and blue, respectively.

        You must solve this problem without using the library's sort
        function.
        """
        # Initialize the pointers: last non-zero element, last non-two
        # element and current element
        last_non_zero_idx = 0
        curr_idx = 0
        last_non_two_idx = len(nums) - 1
        while curr_idx <= last_non_two_idx:
            # If the current element is a 0, switch it with the last
            # non-zero element
            if nums[curr_idx] == 0:
                nums[curr_idx] = nums[last_non_zero_idx]
                nums[last_non_zero_idx] = 0
                last_non_zero_idx += 1
                curr_idx += 1
            # If the current element is a 2, switch it with the last
            # non-two element
            elif nums[curr_idx] == 2:
                nums[curr_idx] = nums[last_non_two_idx]
                nums[last_non_two_idx] = 2
                last_non_two_idx -= 1
            else:
                curr_idx += 1
        return nums
