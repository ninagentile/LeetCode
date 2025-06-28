class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        35. Search Insert Position

        Given a sorted array of distinct integers and a target value,
        return the index if the target is found. If not, return the
        index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.


        Parameters
        ----------
        nums
            List of integers
        target
            Target number

        Returns
        -------
        idx
            Index of the target in the list
        """
        first_idx = 0
        last_idx = len(nums) - 1
        middle_idx = (first_idx + last_idx) // 2

        while first_idx <= last_idx:
            middle_idx = (first_idx + last_idx) // 2
            if nums[middle_idx] == target:
                return middle_idx
            elif nums[middle_idx] > target:
                last_idx = middle_idx - 1
            else:
                first_idx = middle_idx + 1

        if nums[middle_idx] > target:
            return middle_idx
        else:
            return middle_idx + 1
