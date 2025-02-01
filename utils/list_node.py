"""
    List node class
"""


class ListNode:
    def __init__(self, value=0, next_node=None):
        self.value = value
        self.next_node = next_node

    @staticmethod
    def array_to_list_node(arr):
        dummy = ListNode(-1)
        current = dummy
        for number in arr:
            current.next_node = ListNode(number)
            current = current.next_node
        return dummy.next_node

    @staticmethod
    def print_list_node(head):
        while head:
            print(head.value, end=" ")
            head = head.next_node
