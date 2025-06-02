class Solution(object):
    def backspaceCompare(self, s: str, t: str) -> bool:
        """

        Test Result
        844. Backspace String Compare
        Given two strings s and t, return true if they are equal when
        both are typed into empty text editors. '#' means a backspace
        character.

        Note that after backspacing an empty text, the text will
        continue empty.
        """
        s_new = ''
        t_new = ''

        for char in s:
            if char != '#':
                s_new += char
            else:
                s_new = s_new[:-1]
        for char in t:
            if char != '#':
                t_new += char
            else:
                t_new = t_new[:-1]
        if s_new == t_new:
            return True
        else:
            return False
