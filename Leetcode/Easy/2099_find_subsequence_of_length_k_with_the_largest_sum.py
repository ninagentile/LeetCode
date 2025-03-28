class Solution(object):
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        """
        2099. Find Subsequence of Length K With the Largest Sum
        You are given an integer array nums and an integer k. You want
        to find a subsequence of nums of length k that has the largest
        sum.

        Return any such subsequence as an integer array of length k.

        A subsequence is an array that can be derived from another array
        by deleting some or no elements without changing the order of
        the remaining elements.

        Parameters
        ----------
        nums
            List of integers
        k
            Maximum lenght of the subsequence

        Returns
        -------
        subsequence
            Subsequence with the largest sum
        """
        if len(nums) <= k:
            return nums

        max_sum = 0
        curr = 0
        max_window = []
        # Inizialize the window with the first k elements
        for i in range(k):
            curr += nums[i]
            max_window.append(nums[i])

        curr_window = max_window
        for i in range(k, len(nums)):
            # Slide the window
            curr += nums[i]
            curr -= nums[i - k]
            curr_window.append(nums[i])
            # Remove the minimum element
            curr_window.remove(min(curr_window))

            # If the sum is higher than the current max, update the best
            # subsequence
            if curr > max_sum:
                max_sum = curr
                max_window = curr_window

        return max_window
