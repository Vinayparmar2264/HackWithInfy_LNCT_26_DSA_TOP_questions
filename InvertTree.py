# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method 1 :- bfs
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if not root:
#             return root
#         q = deque()
#         q.append(root)
#         while q:
#             e = q.popleft()
#             e.left,e.right = e.right,e.left
#             if e.left:
#                 q.append(e.left)
#             if e.right:
#                 q.append(e.right)  
#         return root  


# method 2 :- dfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left , root.right = root.right,root.left
        return root
