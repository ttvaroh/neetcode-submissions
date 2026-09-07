# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lag = ListNode(None, head)
        curr = head
        pos = 1
        onHead = True

        while curr.next != None and lag.next == head:
            if pos == n:
                break
            curr = curr.next
            pos += 1
        if curr.next != None:
            onHead = False
        while curr.next != None:
            curr = curr.next
            lag = lag.next

        if onHead:
            return head.next
        lag.next = lag.next.next
        return head