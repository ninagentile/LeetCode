class Solution(object):
    def twoSum(self, numbers, target):
        """
        167. Two Sum II - Input Array Is Sorted
        Given a 1-indexed array of integers numbers that is already
        sorted in non-decreasing order, find two numbers such that they
        add up to a specific target number. Let these two numbers be
        numbers[index1] and numbers[index2] where
        1 <= index1 < index2 <= numbers.length.

        Return the indices of the two numbers, index1 and index2, added
        by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution.
        You may not use the same element twice.

        Your solution must use only constant extra space.

        Parameters
        ----------
        numbers
            List of integers
        target
            Target sum

        Returns
        -------
        indexes
            List of indexes (added by one) in nums that sum up to target
        """

        left_idx = 0
        right_idx = len(numbers) - 1
        while left_idx < right_idx:
            total = numbers[left_idx] + numbers[right_idx]
            if total == target:
                return [left_idx + 1, right_idx + 1]
            elif total > target:
                right_idx -= 1
            else:
                left_idx += 1
