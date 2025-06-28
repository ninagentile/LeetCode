class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        """
        268. Missing Number

        Given an array nums containing n distinct numbers in the range
        [0, n], return the only number in the range that is missing from
        the array.

        Parameters
        ----------
        nums
            Array nums containing n distinct numbers in the range [0, n]

        Returns
        -------
        missing_number
            Missing number
        """
        all_nums = set([i for i in range(len(nums) + 1)])
        for n in nums:
            all_nums.remove(n)
        return list(all_nums)[0]
