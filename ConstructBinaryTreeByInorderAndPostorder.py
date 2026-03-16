# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method :- 01
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not inorder or not postorder:
#             return None
        
#         root = TreeNode(postorder.pop())
#         mid = inorder.index(root.val)
#         root.right = self.buildTree(inorder[mid+1:],postorder)
#         root.left = self.buildTree(inorder[:mid],postorder)
        
#         return root

# method :- 02

class Solution:
    def buildTree(self,inorder:List[int],postorder:List[int])->Optional[TreeNode]:
        map_inorder = {val:i for i , val in enumerate(inorder)}

        def helper(l , r):
            if l > r:
                return None
            
            root_val = postorder.pop()
            root = TreeNode(root_val)

            mid = map_inorder[root_val]

            root.right = helper(mid+1,r)
            root.left = helper(l,mid-1)
            return root
        
        return helper(0,len(inorder)-1)
        






