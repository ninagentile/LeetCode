# Definition for singly-linked list.
from typing import Optional

from Leetcode.utils import LinkedList


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(
            self, head: Optional[ListNode], val: int
    ) -> Optional[ListNode]:
        """
        203. Remove Linked List Elements

        Given the head of a linked list and an integer val, remove all
        the nodes of the linked list that has Node.val == val, and
        return the new head.

        Parameters
        ----------
        head
            Optional, head of the linked list
        val
            Value to remove from the list

        Returns
        -------
        head
            Optional, head of the linked list without val
        """
        dummy_head = ListNode(-1)
        dummy_head.next = head
        curr = dummy_head
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy_head.next
