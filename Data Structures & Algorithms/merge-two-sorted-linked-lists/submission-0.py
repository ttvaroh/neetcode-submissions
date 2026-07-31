# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        currMerged = dummy
        curr1 = list1
        curr2 = list2
        while (curr1 and curr2):
            if (curr1.val < curr2.val):
                currMerged.next = curr1
                curr1 = curr1.next
            else:
                currMerged.next = curr2
                curr2 = curr2.next
            currMerged = currMerged.next
        if (curr1):
            currMerged.next = curr1
        else:
            currMerged.next = curr2
        
        return dummy.next
