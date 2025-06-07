from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        82. Remove Duplicates from Sorted List II

        Given the head of a sorted linked list, delete all nodes that
        have duplicate numbers, leaving only distinct numbers from the
        original list. Return the linked list sorted as well.

        Parameters
        head
            Head of the linked list

        Returns
        -------
        head
            Head of the list without nodes with duplicate numbers
        """
        # Case empty list or with just one element
        if (head is None) or (head.next is None):
            return head

        # Use a dummy head
        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        curr = head
        while curr:
            # If the current value is equal to the next, we must remove
            # all such duplicate nodes
            if curr.next and (curr.val == curr.next.val):
                value = curr.val
                # Iterate until a non-duplicate value is found
                while curr and (curr.val == value):
                    curr = curr.next
                # Connect the previous node to the non-duplicate node
                prev.next = curr
                if curr is None:
                    break
                else:
                    continue

            prev = curr
            curr = curr.next
        return dummy_head.next
