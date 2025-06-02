# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
            self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        """
        160. Intersection of Two Linked Lists

        Given the heads of two singly linked-lists headA and headB,
        return the node at which the two lists intersect. If the two
        linked lists have no intersection at all, return null.

        Parameters
        ----------
        headA
            Head of linked list A
        headB
            Head of linked list B

        Returns
        -------
        intersection_node
            The intersection node if Any, None otherwise
        """
        nodes_ids = set()

        # Iterate on list A and save its nodes
        curr = headA
        while curr is not None:
            nodes_ids.add(id(curr))
            curr = curr.next

        # Iterate on list B and check its nodes
        curr = headB
        while curr is not None:
            if id(curr) in nodes_ids:
                return curr
            curr = curr.next

        return None
