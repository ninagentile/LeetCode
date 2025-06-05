from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        234. Palindrome Linked List

        Given the head of a singly linked list, return true if it is a
        palindrome or false otherwise.
        """
        # Get the values of the list
        curr = head
        values = []
        while curr is not None:
            values.append(curr.val)
            curr = curr.next

        # Check if the list is a palindrome using two pointers
        left = 0
        right = len(values) - 1
        while left <= right:
            if values[left] != values[right]:
                return False
            left += 1
            right -= 1
        return True

    def isPalindromeOptimized(self, head: Optional[ListNode]) -> bool:
        """
        Solution in O(1) space
        """
        if head is None:
            return True

        # Get to the half of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the remaining list
        prev, curr = slow, slow.next
        prev.next = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # Compare the two halves
        new_head = prev
        curr = head
        while new_head:
            if curr.val != new_head.val:
                return False
            curr = curr.next
            new_head = new_head.next
        return True
