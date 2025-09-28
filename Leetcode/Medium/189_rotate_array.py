class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        189. Rotate Array

        Given an integer array nums, rotate the array to the right by k
        steps, where k is non-negative.

        Example 1:
        Input: nums = [1,2,3,4,5,6,7], k = 3
        Output: [5,6,7,1,2,3,4]
        Explanation:
        rotate 1 steps to the right: [7,1,2,3,4,5,6]
        rotate 2 steps to the right: [6,7,1,2,3,4,5]
        rotate 3 steps to the right: [5,6,7,1,2,3,4]

        Example 2:
        Input: nums = [-1,-100,3,99], k = 2
        Output: [3,99,-1,-100]
        Explanation:
        rotate 1 steps to the right: [99,-1,-100,3]
        rotate 2 steps to the right: [3,99,-1,-100]
        """
        # Compute the minimum number of rotations: if len(nums) = 5 and
        # k = 19, then the effective number of rotations is 4
        n_rotations = k % len(nums)

        # If no rotations are needed, return
        if n_rotations == 0:
            return

        # In all the other cases, rotate the array of n_rotations
        last_n_elements = nums[-n_rotations:]
        new_array = [*last_n_elements, *nums[:-n_rotations]]
        for idx, i in enumerate(new_array):
            nums[idx] = i
