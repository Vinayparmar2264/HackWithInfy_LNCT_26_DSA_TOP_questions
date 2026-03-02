# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        temp = head
        prev = dummy
        while temp and temp.next:
            if temp.val == temp.next.val:
                while temp and temp.next and temp.val==temp.next.val:
                    temp = temp.next
                temp=temp.next
                prev.next = temp
            else:
                prev =temp
                temp = temp.next
        return dummy.next
