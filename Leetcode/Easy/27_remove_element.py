class Solution(object):
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        27. Remove Element
        Given an integer array nums and an integer val, remove all
        occurrences of val in nums in-place. The order of the elements
        may be changed. Then return the number of elements in nums which
        are not equal to val.
        Consider the number of elements in nums which are not equal to
        val be k, to get accepted, you need to do the following things:
        Change the array nums such that the first k elements of nums
        contain the elements which are not equal to val. The remaining
        elements of nums are not important as well as the size of nums.
        Return k.

        Parameters
        ----------
        nums
            List of numbers
        val
            Value to remove from numbers

        Returns
        -------
        count
            Number of elements in num that are different from val
        """

        i = 0
        j = 1
        while i < len(nums):

            # If the current number is val, it must be removed by
            # switching it with the first number different from val
            while nums[i] == val:

                if j < i:
                    j = i + 1

                # Return i when arrived at the last element
                if j == len(nums):
                    return i

                # Switch the current number with the j-th number
                nums[i] = nums[j]
                nums[j] = val
                j += 1

            i += 1
