"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # method 1
        
        my_dict = {}
        if head==None:
            return None
        curr = head
        prev = None
        newHead = None

        while curr:
            temp = Node(curr.val)
            my_dict[curr]=temp
            if newHead is None:
                newHead = temp
                prev = newHead
            else:
                prev.next = temp
                prev = temp
            curr = curr.next
            
# fill random points
        curr = head
        newCurr = newHead
        while curr:
            if curr.random == None:
                newCurr.random=None
            else:
                randomOriginal = curr.random
                deepCopyCorrespondingRandom = my_dict[randomOriginal]
                newCurr.random =deepCopyCorrespondingRandom
            curr = curr.next
            newCurr = newCurr.next
        return newHead




        
# method 2

        
        if head==None:
            return None
        
        curr = head
        while curr:
            currNext = curr.next
            curr.next = Node(curr.val)
            curr.next.next = currNext

            curr = currNext

        curr = head
        while curr and curr.next:
            if curr.random ==None:
                curr.next.random = None
            else:
                curr.next.random = curr.random.next
            curr= curr.next.next

        newHead =  head.next
        newCurr= newHead
        curr = head

        while curr and newCurr:
            if curr.next:
                curr.next = curr.next.next
            else:
                curr.next = None
            
            if newCurr.next:
                newCurr.next = newCurr.next.next
            else:
                newCurr.next = None
            curr = curr.next
            newCurr = newCurr.next
        return newHead




