# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []
        idx =-1

        def reverse(level):
            l = 0
            r = len(level)-1
            while l<r:
                level[l],level[r] =level[r],level[l]
                l+=1
                r-=1
            return level

        while queue:
            size = len(queue)
            idx+=1
            level = []
            for i in range(size):
                e = queue.popleft()
                level.append(e.val)      
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            
            if idx%2==0:
                res.append(level)
            else:
                res.append(reverse(level))

        return res



# method 2 
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        res = []
        left_to_right = True

        while queue:
            size = len(queue)
            level = deque()

            for _ in range(size):
                node = queue.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(list(level))
            left_to_right = not left_to_right

        return res
