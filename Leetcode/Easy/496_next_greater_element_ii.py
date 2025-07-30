class Solution:
    def nextGreaterElement(
        self, nums1: list[int], nums2: list[int]
    ) -> list[int]:
        """
        496. Next Greater Element I

        The next greater element of some element x in an array is the
        first greater element that is to the right of x in the same
        array.

        You are given two distinct 0-indexed integer arrays nums1 and
        nums2, where nums1 is a subset of nums2.

        For each 0 <= i < nums1.length, find the index j such that
        nums1[i] == nums2[j] and determine the next greater element of
        nums2[j] in nums2. If there is no next greater element, then the
        answer for this query is -1.

        Return an array ans of length nums1.length such that ans[i] is
        the next greater element as described above.
        """
        # Use a monothonic stack and save, for each element in nums2,
        # the greater in the array
        stack = []
        mapping = {}
        for elem in reversed(nums2):
            mapping[elem] = -1
            # Pop until a greater element is found or the stack
            # becomes empty
            while len(stack) and stack[-1] < elem:
                stack.pop()
            # Save the greater element (if any)
            if len(stack):
                mapping[elem] = stack[-1]

            stack.append(elem)

        # Find the greater element for each element in nums1
        solution = []
        for elem in nums1:
            solution.append(mapping[elem])
        return solution
