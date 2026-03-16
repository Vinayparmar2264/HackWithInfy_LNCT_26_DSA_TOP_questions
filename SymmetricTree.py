# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# method :1
# from collections import deque

# class Solution:

#     def left_subtree(self, node, q):
#         if not node:
#             return
        
#         self.left_subtree(node.left, q)
#         q.append(node.val)
#         self.left_subtree(node.right, q)


#     def right_subtree(self, node, q):
#         if not node:
#             return True
        
#         if not self.right_subtree(node.right, q):
#             return False

#         if not q or q.popleft() != node.val:
#             return False

#         if not self.right_subtree(node.left, q):
#             return False

#         return True


#     def isSymmetric(self, root):
#         if not root:
#             return True

#         q = deque()

#         # store left subtree
#         self.left_subtree(root.left, q)

#         # compare with mirrored right subtree
#         return self.right_subtree(root.right, q)


# method 2





class Solution:
    def isMirror(self, t1, t2):

        if not t1 and not t2:
            return True

        if not t1 or not t2:
            return False

        return (
            t1.val == t2.val
            and self.isMirror(t1.left, t2.right)
            and self.isMirror(t1.right, t2.left)
        )


    def isSymmetric(self, root):
        return self.isMirror(root.left, root.right)
