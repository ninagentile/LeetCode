from collections import Counter


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        169. Majority Element

        Given an array nums of size n, return the majority element.

        The majority element is the element that appears more than
        ⌊n / 2⌋ times. You may assume that the majority element always
        exists in the array.

        Parameters
        ----------
        nums
            Array of elements

        Returns
        -------
        majority_element
        """
        counter = Counter(nums)
        n = len(nums) / 2
        for element, count in counter.items():
            if count >= n:
                return element
