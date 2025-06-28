# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self, head: ListNode | None):
        self.head = head

    def add(self, value):
        node = ListNode(val=value)
        node.next = self.head
        self.head = node

    def print_list(self):
        curr = self.head
        values = []
        while curr is not None:
            values.append(curr.val)
            curr = curr.next
        values.append(None)
        print(' -> '.join([str(v) for v in values]))

    def size(self):
        curr = self.head
        size = 0
        while curr is not None:
            curr = curr.next
            size += 1
        return size

    @staticmethod
    def initialize_from_list(values: list) -> 'LinkedList':
        ll = LinkedList(None)
        for v in reversed(values):
            ll.add(v)
        return ll
