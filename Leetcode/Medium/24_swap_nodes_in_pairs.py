from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        24. Swap Nodes in Pairs

        Given a linked list, swap every two adjacent nodes and return
        its head. You must solve the problem without modifying the
        values in the list's nodes (i.e., only nodes themselves may be
        changed.)

        Parameters
        ----------
        head
            Head of the linked list

        Returns
        -------
        head
            Head of the swapped list
        """
        # Case empty list or with just one element
        if (head is None) or (head.next is None):
            return head

        # Add a dummy node as head of the list
        dummy_node = ListNode()
        dummy_node.next = head
        prev_node = dummy_node
        curr = head
        while curr:
            # Do not swap the last element
            if curr.next is None:
                break

            # Swap the nodes: the next points to curr, curr points to
            # next.next, prev points to next
            next_node = curr.next
            prev_node.next = next_node
            curr.next = next_node.next
            next_node.next = curr

            # Update the nodes
            prev_node = curr
            curr = curr.next

        # Return the head of the list
        return dummy_node.next
