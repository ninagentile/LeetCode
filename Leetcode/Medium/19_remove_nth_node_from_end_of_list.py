from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(
            self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        """
        19. Remove Nth Node From End of List

        Given the head of a linked list, remove the nth node from the
        end of the list and return its head.

        Parameters
        ----------
        head
            Head of the linked list
        n
            nth node from the end to be removed

        Returns
        -------
        head
            Head of the list without the nth node from the end
        """
        curr = head
        # Save the nodes in a list
        list_of_nodes = []
        while curr:
            list_of_nodes.append(curr)
            curr = curr.next

        n_nodes = len(list_of_nodes)
        idx_to_remove = n_nodes - n

        # Case remove the first element: the head becomes the next node
        # (if any)
        if idx_to_remove == 0:
            if n_nodes >= 2:
                return list_of_nodes[1]
            else:
                return None

        # Case remove the last element: the previous node points to None
        if n == 1:
            list_of_nodes[idx_to_remove - 1].next = None
        # Case element in the middle of the list: the previous node
        # points to the next node
        else:
            list_of_nodes[idx_to_remove - 1].next = list_of_nodes[idx_to_remove + 1]

        return head

