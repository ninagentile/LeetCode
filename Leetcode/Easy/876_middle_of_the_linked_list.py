# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):

    @staticmethod
    def get_list_size(head: ListNode | None) -> int:
        curr = head
        size = 0
        while curr is not None:
            curr = curr.next
            size += 1
        return size

    def middleNode(self, head: ListNode | None) -> ListNode | None:
        """
        876. Middle of the Linked List
        Given the head of a singly linked list, return the middle node
        of the linked list.

        If there are two middle nodes, return the second middle node.

        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Compute the size of the list
        size = self.get_list_size(head)
        # Get the index of the node to retrieve
        idx = int(size / 2)

        # Now get the element at the computed index
        curr = head
        curr_idx = 0
        while curr is not None:
            # When we arrive at the correct index, return the current
            # node
            if curr_idx == idx:
                return curr
            # Otherwise, update the current node and the current index
            curr = curr.next
            curr_idx += 1
