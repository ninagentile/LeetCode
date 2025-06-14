from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(
        self, head: Optional[ListNode], x: int
    ) -> Optional[ListNode]:
        """
        86. Partition List

        Given the head of a linked list and a value x, partition it such
        that all nodes less than x come before nodes greater than or
        equal to x.

        You should preserve the original relative order of the nodes in
        each of the two partitions

        Parameters
        ----------
        head
            Head of the linked list
        x
            Value to use for partitioning

        Returns
        -------
        head
            Head of the partitioned list
        """
        if (not head) or (not head.next):
            return head

        # Create two lists: one with the values lower than x, one with
        # the ones greater than or equal to x.
        lower_values = []
        greater_values = []
        curr = head
        while curr:
            if curr.val < x:
                lower_values.append(curr.val)
            else:
                greater_values.append(curr.val)
            curr = curr.next

        # Create a new list inserting first the lower values and then
        # the greater values
        if len(lower_values) > 0:
            prev = ListNode(lower_values[0])
            head = prev
            for val in lower_values[1:]:
                node = ListNode(val)
                prev.next = node
                prev = node
        # If there are no lower values, the list is already partitioned
        else:
            return head

        # Insert the greater values
        for val in greater_values:
            node = ListNode(val)
            prev.next = node
            prev = node

        return head
