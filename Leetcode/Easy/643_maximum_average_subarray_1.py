class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        current_sum = 0
        mean = 0
        for i in range(len(nums)):
            if i >= k:
                # Compute and update the mean
                mean = max(current_sum / k, mean)

                # Update the window
                current_sum -= nums[i - k]

            # Add current number to the window
            current_sum += nums[i]
        # Update the mean with the last element
        mean = max(current_sum / k, mean)
        return mean
