from typing import Optional


class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


class Solution:

    def list_to_link(self, n1: [int], n2: [int]):
        l1 = ListNode(n1[0])
        current_l1 = l1
        for i in range(1, len(n1)):
            current_l1.next = n1[i]
            current_l1 = current_l1.next
        l2 = ListNode(n2[0])
        current_l2 = l2
        for i in range(1, len(n2)):
            current_l2.next = n2[i]
            current_l2 = current_l2.next

    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        current_node1 = l1
        current_node2 = l2
        total = ListNode()
        current = total
        carry = 0

        while True:

            val1 = current_node1.val if current_node1 else 0
            val2 = current_node2.val if current_node2 else 0

            current.val = (val1 + val2 + carry) % 10
            carry = (carry + val1 + val2) // 10

            current_node1 = current_node1.next if current_node1 else 0
            current_node2 = current_node2.next if current_node2 else 0

            if not current_node1 and not current_node2 and not carry:
                break

            current.next = ListNode()
            current = current.next

        return total
