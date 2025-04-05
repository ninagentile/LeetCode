import collections


class Solution(object):
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """
        15. 3Sum
        Given an integer array nums, return all the triplets
        [nums[i], nums[j], nums[k]] such that i != j, i != k, and
        j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        """
        counts = collections.Counter(nums)
        nums = sorted(nums)
        solutions = []
        prev_first_num = None
        prev_last_num = None
        for first in range(0, len(nums) - 1):
            # Skip duplicates
            if (prev_first_num is not None) and (
                    nums[first] == prev_first_num):
                continue
            for last in reversed(range(first + 1, len(nums))):
                # Skip duplicates
                if (prev_last_num is not None) and (
                        nums[last] == prev_last_num):
                    continue
                partial_sum = nums[first] + nums[last]

                # Skip seen solutions
                if (-partial_sum < nums[first]) or (-partial_sum > nums[last]):
                    prev_last_num = nums[last]
                    continue

                counts[nums[first]] -= 1
                counts[nums[last]] -= 1
                # If the complement is in nums, save this triplet
                if counts.get(-partial_sum, 0) > 0:
                    solutions.append([nums[first], -partial_sum, nums[last]])

                # Reset counters
                counts[nums[first]] += 1
                counts[nums[last]] += 1

                prev_last_num = nums[last]
            prev_first_num = nums[first]

        return solutions
