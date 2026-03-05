# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = 0
        self.ans = None

    def inorder(self, node, k):
        if node is None:
            return
        
        # Traverse left
        self.inorder(node.left, k)

        # Visit node
        self.count += 1
        if self.count == k:
            self.ans = node.val
            return
        
        # Traverse right
        self.inorder(node.right, k)

    def kthSmallest(self, root, k):
        self.inorder(root, k)
        return self.ans
