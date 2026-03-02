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


