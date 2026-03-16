# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method 1

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []
        idx =-1
        while queue:
            size = len(queue)
            idx+=1
            res.append([])
            for i in range(size):
                e = queue.popleft()
                res[idx].append(e.val)        
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
        return res


# meethod 2

# from collections import deque

# class Solution:
#     def levelOrder(self, root):
#         if not root:
#             return []

#         queue = deque([root])
#         res = []

#         while queue:
#             size = len(queue)
#             level = []

#             for _ in range(size):
#                 node = queue.popleft()
#                 level.append(node.val)

#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)

#             res.append(level)

#         return res
