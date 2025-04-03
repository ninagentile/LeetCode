class Solution(object):
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """
        977. Squares of a Sorted Array
        Given an integer array nums sorted in non-decreasing order,
        return an array of the squares of each number sorted in
        non-decreasing order.

        Parameters
        ----------
        nums
            List of integers sorted in non-decreasing order

        Returns
        -------
        squares
            List of squares of the numbers in nums sorted in
            non-decreasing order
        """
        left_idx = 0
        right_idx = len(nums) - 1
        squares_idx = len(nums) - 1
        # Create an array to store the squares
        squares = [0] * len(nums)

        # Loop until all the elements in the squares array are filled
        while squares_idx >= 0:

            left = nums[left_idx] ** 2
            right = nums[right_idx] ** 2
            # If the right number is greater than the left, then add it
            # to the squares array and move its pointer
            if right > left:
                squares[squares_idx] = right
                right_idx -= 1
            # Otherwise, add the left number to the squares array and
            # move its pointer
            else:
                squares[squares_idx] = left
                left_idx += 1

            # Update the index of the squares array
            squares_idx -= 1
        return squares
