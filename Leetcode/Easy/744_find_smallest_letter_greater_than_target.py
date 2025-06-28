class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        """
        744. Find Smallest Letter Greater Than Target

        You are given an array of characters letters that is sorted in
        non-decreasing order, and a character target. There are at least
        two different characters in letters.

        Return the smallest character in letters that is lexicographically
        greater than target. If such a character does not exist, return
        the first character in letters.


        Parameters
        ----------
        letters
            Sorted array of characters
        target
            Character

        Returns
        -------
        smaller_char
            Smallest character in letters that is lexicographically
            greater than target
        """
        first_idx = 0
        last_idx = len(letters) - 1

        while first_idx < last_idx:
            middle_idx = (first_idx + last_idx) // 2
            curr_letter = letters[middle_idx]
            if curr_letter <= target:
                first_idx = middle_idx + 1
            else:
                last_idx = middle_idx

        if letters[last_idx] > target:
            return letters[last_idx]
        return letters[0]
