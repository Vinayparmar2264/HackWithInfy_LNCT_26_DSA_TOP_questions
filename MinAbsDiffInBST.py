# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method 1

# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
#         arr = []
#         def Inorder(root):
#             if not root :
#                 return 
            
#             Inorder(root.left)
#             arr.append(root.val)
#             Inorder(root.right)

#         Inorder(root)
#         min_diff = min(arr[i] - arr[i-1] for i in range(1, len(arr)))
#         return min_diff





#method 2 

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.ans = float('inf')
        
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            if self.prev :
                self.ans = min(self.ans, root.val - self.prev.val)
            self.prev = root
            inorder(root.right)
            return
        
        inorder(root)
        return self.ans
