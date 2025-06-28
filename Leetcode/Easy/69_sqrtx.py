class Solution:
    def mySqrt(self, x: int) -> int:
        """
        69. Sqrt(x)

        Given a non-negative integer x, return the square root of x
        rounded down to the nearest integer. The returned integer should
        be non-negative as well.

        You must not use any built-in exponent function or operator.

        For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python

        Parameters
        ----------
        x
            Number for which we want to compute the square root

        Returns
        -------
        sqrt
            Square root of x rounded down to the nearest integer
        """
        if x <= 1:
            return x

        # Use binary search to find the square root of x
        first = 1
        last = x
        while first <= last:
            # Get the number in the middle of the range [first, last]
            sqr = (last + first) // 2
            # Check its power
            pow = sqr * sqr
            if pow == x:
                return sqr
            # Update the range in which we look for the square root
            elif pow > x:
                last = sqr - 1
            else:
                first = sqr + 1
        return last
