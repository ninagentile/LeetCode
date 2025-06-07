from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        445. Add Two Numbers II

        You are given two non-empty linked lists representing two
        non-negative integers. The most significant digit comes first
        and each of their nodes contains a single digit. Add the two
        numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero,
        except the number 0 itself.

        Parameters
        ----------
        l1
            Head of list 1
        l2
            Head of list 2

        Returns
        -------
        list
            List containing the sum of the two lists
        """
        if (l1 is None) or (l1.val == 0):
            return l2
        if (l2 is None) or (l2.val == 0):
            return l1

        # Extract the number that each list represents
        val1 = self._get_number_from_list(l1)
        val2 = self._get_number_from_list(l2)

        # Compute the total
        total = val1 + val2
        prev = None
        node = None

        # Create a list representing the total
        while total > 0:
            val = total % 10
            total = total // 10
            node = ListNode(val)
            node.next = prev
            prev = node
        return node

    @staticmethod
    def _get_number_from_list(l1: ListNode) -> int:
        """
        Extracts the number the input list represents

        Parameters
        ----------
        l1
            Head of the list

        Returns
        -------
        value
            Value of the list
        """
        value = 0
        while l1:
            if value != 0:
                value *= 10
            value += l1.val
            l1 = l1.next

        return value
