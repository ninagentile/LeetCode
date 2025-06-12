from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(
        self, head: Optional[ListNode], k: int
    ) -> Optional[ListNode]:
        """
        61. Rotate List

        Given the head of a linked list, rotate the list to the right by
        k places.

        Parameters
        ----------
        head
        k

        Returns
        -------

        """
        if k == 0:
            return head

        curr = head
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next

        if len(values) <= 1:
            return head

        # No need to rotate if k is a multiple of the list lenght
        k = k % len(values)
        if k == 0:
            return head

        # Add k dummy nodes at the start of the list
        prev_head = head
        for _ in range(k):
            node = ListNode()
            node.next = head
            head = node

        # Iterate until the new end of the list
        curr = prev_head
        last_node = None
        for idx in range(len(values) - k):
            # Save a reference to the last node of the list
            if idx == len(values) - k - 1:
                last_node = curr
            curr = curr.next

        # All the dummy nodes are initialized with the values from curr
        # until the end of the list
        new_node = head
        for _ in range(k):
            new_node.val = curr.val
            curr = curr.next
            new_node = new_node.next

        # Make the last node point to None
        last_node.next = None
        return head
