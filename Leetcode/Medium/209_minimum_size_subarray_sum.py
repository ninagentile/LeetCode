class Solution(object):
    def minSubArrayLen(self, target, nums):
        min_lenght_subarray = float('inf')
        first = 0
        last = 0
        window_sum = 0
        window_debug = []

        while last < len(nums):
            window_sum += nums[last]
            window_debug.append(nums[last])

            # Shrink until window_sum < target
            while window_sum >= target:
                min_lenght_subarray = min(
                    min_lenght_subarray, last - first + 1
                )
                window_sum -= nums[first]
                window_debug.pop(0)
                first += 1
                if first > last:
                    break
            last += 1

        if min_lenght_subarray == float('inf'):
            return 0

        return min_lenght_subarray
