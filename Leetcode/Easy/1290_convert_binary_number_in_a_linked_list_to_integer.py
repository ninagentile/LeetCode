from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        1290. Convert Binary Number in a Linked List to Integer

        Given head which is a reference node to a singly-linked list.
        The value of each node in the linked list is either 0 or 1. The
        linked list holds the binary representation of a number.

        Return the decimal value of the number in the linked list.

        The most significant bit is at the head of the linked list.

        Parameters
        ----------
        head
            Head of the linked list

        Returns
        -------
        value
            The decimal value of the number in the linked list.
        """
        # Get the values of the list
        values = []
        size = 0
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
            size += 1

        # Get the decimal value
        decimal_value = 0
        for i, value in enumerate(reversed(values)):
            # Avoid 0^0 to return 1
            if i == 0:
                decimal_value += value
            else:
                decimal_value += (2 * value) ** i
        return decimal_value
