class Solution(object):
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        392. Is Subsequence
        Given two strings s and t, return true if s is a subsequence of
        t, or false otherwise.

        A subsequence of a string is a new string that is formed from the
        original string by deleting some (can be none) of the characters
        without disturbing the relative positions of the remaining
        characters. (i.e., "ace" is a subsequence of "abcde" while
        "aec" is not).

        Parameters
        ----------
        s, t
            Strings

        Returns
        -------
        is_subsequence
            Boolean, True if s is subsequence of t, False otherwise
        """

        s_idx = 0

        if len(t) < len(s):
            return False

        if len(s) == 0:
            return True

        for t_idx in range(len(t)):
            if t[t_idx] == s[s_idx]:
                s_idx += 1

                if s_idx == len(s):
                    return True
        return False
