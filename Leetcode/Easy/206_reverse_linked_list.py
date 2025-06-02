from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        206. Reverse Linked List

        Given the head of a singly linked list, reverse the list, and
        return the reversed list.

        Parameters
        ----------
        head
            Head of the linked list

        Returns
        -------
        head
            Head of the reversed list
        """
        if head is None:
            return head

        prev = head
        curr = head.next
        # The first element of the list will become the last, so set its
        # next pointer to None
        prev.next = None
        # Iterate on the list
        while curr is not None:
            # Set the next of the current node to the previous node
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Return prev, that is now the head of the reversed list
        return prev
