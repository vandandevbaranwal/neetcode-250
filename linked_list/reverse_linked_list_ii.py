# Pattern: Linked List Manipulation + Reverse Sublist
# Trigger: "reverse a portion of a linked list" = isolate, reverse, reconnect

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(
        self,
        head: Optional[ListNode],
        left: int,
        right: int
    ) -> Optional[ListNode]:

        # dummy node handles edge case when left = 1
        dummy = ListNode(0)
        dummy.next = head

        # move prev to the node before the sublist
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        # identify the sublist
        sublist_head = prev.next
        sublist_tail = sublist_head

        for _ in range(right - left):
            sublist_tail = sublist_tail.next

        # save the node after the sublist
        next_node = sublist_tail.next

        # disconnect the sublist
        sublist_tail.next = None

        # reverse the isolated sublist
        reversed_sublist = self.reverseList(sublist_head)

        # reconnect
        prev.next = reversed_sublist
        sublist_head.next = next_node

        return dummy.next

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive linked list reversal

        if not head:
            return None

        newHead = head

        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead