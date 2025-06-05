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
        2. Add Two Numbers

        You are given two non-empty linked lists representing two
        non-negative integers. The digits are stored in reverse order,
        and each of their nodes contains a single digit. Add the two
        numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero,
        except the number 0 itself.

        Parameters
        ----------
        l1:
            Linked list 1
        l2:
            Linked list 2

        Returns
        -------
        sum
            Sum of the two lists
        """
        l1_curr = l1
        l2_curr = l2
        prev_node: Optional[ListNode] = None
        new_head: Optional[ListNode] = None
        carry = 0
        while l1_curr or l2_curr:
            if l1_curr:
                val1 = l1_curr.val
                l1_curr = l1_curr.next
            else:
                val1 = 0
            if l2_curr:
                val2 = l2_curr.val
                l2_curr = l2_curr.next
            else:
                val2 = 0

            tot = val1 + val2 + carry
            value = tot % 10
            carry = int(tot / 10)

            new_node = ListNode(val=value)
            if prev_node is None:
                new_head = new_node
            else:
                prev_node.next = new_node
            prev_node = new_node

        if carry > 0:
            new_node = ListNode(val=carry)
            prev_node.next = new_node

        return new_head
