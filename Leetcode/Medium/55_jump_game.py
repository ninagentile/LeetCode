class Solution:
    def canJump(self, nums: list[int]) -> bool:
        """
        55. Jump Game

        You are given an integer array nums. You are initially
        positioned at the array's first index, and each element in the
        array represents your maximum jump length at that position.

        Return true if you can reach the last index, or false otherwise.

        Example 1:
        Input: nums = [2,3,1,1,4]
        Output: true
        Explanation: Jump 1 step from index 0 to 1, then 3 steps to the
        last index.

        Example 2:
        Input: nums = [3,2,1,0,4]
        Output: false
        Explanation: You will always arrive at index 3 no matter what.
        Its maximum jump length is 0, which makes it impossible to reach
        the last index.

        Parameters
        ----------
        nums
            Array of numbers

        Returns
        -------
        can_jump
            True if you can reach the last index, False otherwise.
        """
        if nums[0] == 0:
            if len(nums) == 1:
                return True
            else:
                return False

        # Traverse the array backwards to see if there is an element
        # that allows me to reach the last index. If such an element
        # exists, I look for another element that allows me to reach the
        # current index, and so on until I finish traversing the array.
        curr_jump_distance = 1
        curr_idx = len(nums) - 2
        while curr_idx >= 0:
            # If from this index I can jump at least curr_jump_distance
            # times, I reset the curr_jump_distance (I want to look for
            # a new element from which I can reach this index)
            if nums[curr_idx] >= curr_jump_distance:
                curr_jump_distance = 1
            # Otherwise, I increase the curr_jump_distance
            else:
                curr_jump_distance += 1
                # If I am at the end of the array and still cannot reach
                # the last index, return False
                if curr_idx == 0:
                    return False
            # Go backwards
            curr_idx -= 1
        return True
