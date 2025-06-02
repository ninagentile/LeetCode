from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        83. Remove Duplicates from Sorted List

        Given the head of a sorted linked list, delete all duplicates
        such that each element appears only once. Return the linked list
        sorted as well.

        Parameters
        ----------
        head
            Head of the linked list

        Returns
        -------
        head
            Head of the updated linked list
        """
        if head is None:
            return head

        curr = head.next
        prev = head
        while prev is not None:
            if (curr is None) or (prev.val != curr.val):
                # When a non-duplicated element is found, link prev to
                # curr and update prev
                prev.next = curr
                prev = curr

                # Break at the end of the list
                if prev is None:
                    break

            curr = curr.next
        return head
