class Solution:
    def isValid(self, s: str) -> bool:
        """
        20. Valid Parentheses
        Given a string s containing just the characters '(', ')', '{',
         '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Every close bracket has a corresponding open bracket of the same type.

        Parameters
        ----------
        s
            String to check

        Returns
        -------
        is_valid
            True if the string is valid, False otherwise
        """
        stack = []
        open_parenthesis = {'(', '[', '{'}
        parenthesis_mapping = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in open_parenthesis:
                stack.append(char)
            else:
                # If the last parenthesis is of the same type and it is opening, then it is ok
                if len(stack) and (stack[-1] == parenthesis_mapping[char]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
