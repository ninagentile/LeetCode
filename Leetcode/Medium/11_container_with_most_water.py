class Solution(object):
    def maxArea(self, height: list[int]) -> int:
        """
        11. Container With Most Water
        You are given an integer array height of length n. There are n
        vertical lines drawn such that the two endpoints of the ith line
        are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container,
        such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.
        """

        first = 0
        last = len(height) - 1
        max_amount = 0
        while first != last:
            min_height = min(height[first], height[last])
            distance = last - first
            amount = min_height * distance

            # Update max_amount
            max_amount = max(max_amount, amount)

            # Move the pointer of the lowest number
            if height[first] > height[last]:
                last -= 1
            else:
                first += 1

        return max_amount
