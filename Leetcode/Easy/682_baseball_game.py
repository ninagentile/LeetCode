class Solution:
    def calPoints(self, operations: list[str]) -> int:
        """
        682. Baseball Game
        You are keeping the scores for a baseball game with strange
        rules. At the beginning of the game, you start with an empty
        record.

        You are given a list of strings operations, where operations[i]
        is the ith operation you must apply to the record and is one of
        the following:

        An integer x.
        Record a new score of x.
        '+'.
        Record a new score that is the sum of the previous two scores.
        'D'.
        Record a new score that is the double of the previous score.
        'C'.
        Invalidate the previous score, removing it from the record.
        Return the sum of all the scores on the record after applying
        all the operations.

        The test cases are generated such that the answer and all
        intermediate calculations fit in a 32-bit integer and that all
        operations are valid.

        Parameters
        ----------
        operations
            List of operations

        Returns
        -------
        score
            Final score
        """
        stack = []
        for op in operations:
            # if the operation is +, sum the last two scores and store it
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            # if the operation is D, double the last and store it
            elif op == 'D':
                stack.append(stack[-1] * 2)
            # if the operation is C, remove the last score
            elif op == 'C':
                stack.pop()
            # if the operation is an integer, store it
            else:
                stack.append(int(op))

        # Sum all the scores and return it
        return sum(stack)
