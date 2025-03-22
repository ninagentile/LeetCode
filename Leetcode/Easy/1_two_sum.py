class Solution(object):
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Given an array of integers nums and an integer target, return
        indices of the two numbers such that they add up to target.

        Use a dictionary to map the index of each element in the list.
        Look for the complement of the current element; if it is found,
        return a list made of the current index and the index of the
        complement

        Parameters
        ----------
        nums
            List of integers
        target
            Target

        Returns
        -------
        indexes
            List of indexes of the numbers in num that sum up to target

        """
        number_to_index_mapping = {}

        for idx, num in enumerate(nums):
            complement = target - num

            if complement in number_to_index_mapping:
                return [idx, number_to_index_mapping[complement]]

            number_to_index_mapping[num] = idx

        return []
