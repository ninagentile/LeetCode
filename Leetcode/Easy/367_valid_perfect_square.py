class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        """
        367. Valid Perfect Square

        Given a positive integer num, return true if num is a perfect
        square or false otherwise.

        A perfect square is an integer that is the square of an integer.
        In other words, it is the product of some integer with itself.

        You must not use any built-in library function, such as sqrt.

        Parameters
        ----------
        num
            Number to check

        Returns
        -------
        is_perfect_square
            True if num is a perfect square or False otherwise.
        """
        first = 1
        last = num
        while first <= last:
            middle = (first + last) // 2
            power = middle * middle
            if power == num:
                return True
            elif power > num:
                last = middle - 1
            else:
                first = middle + 1

        return False
