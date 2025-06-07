class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode) -> None:
        """
        237. Delete Node in a Linked List

        There is a singly-linked list head and we want to delete a node
        `node` in it.

        You are given the node to be deleted node. You will not be given
        access to the first node of head.

        All the values of the linked list are unique, and it is
        guaranteed that the given node node is not the last node in the
        linked list.

        Delete the given node. Note that by deleting the node, we do not
        mean removing it from memory. We mean:
        The value of the given node should not exist in the linked list.
        The number of nodes in the linked list should decrease by one.
        All the values before node should be in the same order.
        All the values after node should be in the same order.
        """
        # Copy the value of each node in the previous node
        while node.next:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
                break
            node = node.next

    def delete_node_optimized(self, node: ListNode) -> None:
        # Copy the value of the next node inside the node to remove
        node.val = node.next.val
        # Link the node to the remaining part of the list
        node.next = node.next.next
