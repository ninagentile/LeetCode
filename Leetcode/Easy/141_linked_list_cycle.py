from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        141. Linked List Cycle

        Given head, the head of a linked list, determine if the linked
        list has a cycle in it.

        There is a cycle in a linked list if there is some node in the
        list that can be reached again by continuously following the
        next pointer. Internally, pos is used to denote the index of the
        node that tail's next pointer is connected to. Note that pos is
        not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise,
        return false.

        Parameters
        ----------
        head
            Pointer to the head of the linked list

        Returns
        -------
        has_cycle
            True if the linked list has a cycle, False otherwise
        """
        # Use the Floyd’s Cycle-Finding Algorithm: one pointer moves one
        # step at a time, another two steps at a time. If they meet,
        # then there is a cycle. If the faster pointer is None, there is
        # no cycle
        slow_pointer = head
        fast_pointer = head
        while (fast_pointer is not None) and (fast_pointer.next is not None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

            if fast_pointer == slow_pointer:
                return True

        return False
