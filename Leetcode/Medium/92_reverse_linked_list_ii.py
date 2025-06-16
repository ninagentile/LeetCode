from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        """
        92. Reverse Linked List II

        Given the head of a singly linked list and two integers left and
        right where left <= right, reverse the nodes of the list from
        position left to position right, and return the reversed list.

        Parameters
        ----------
        head
            Head of the linked list
        left
            The starting position to reverse
        right
            The ending position to reverse

        Returns
        -------
        head
            Head of the linked list with the specified range reversed
        """
        if (head is None) or (head.next is None) or (left == right):
            return head

        idx = 1
        left_node = None
        curr = head
        values_between = []
        while idx <= right:
            if idx >= left:
                if idx == left:
                    left_node = curr
                values_between.append(curr.val)
            curr = curr.next
            idx += 1

        # Reverse the values
        for val in reversed(values_between):
            left_node.val = val
            left_node = left_node.next

        return head
