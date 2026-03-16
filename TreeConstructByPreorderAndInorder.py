# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# method :- 01

# class Solution:
#     def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
#         if not preorder or not inorder:
#             return None
        
#         root = TreeNode(preorder.pop(0))
#         mid = inorder.index(root.val)
#         root.left = self.buildTree(preorder,inorder[:mid])
#         root.right = self.buildTree(preorder,inorder[mid+1:])

#         return root



# method :- 02
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        map_inorder = {val:i for i , val in enumerate(inorder)}

        def helper(l , r):
            if l > r:
                return None
            
            root_val = preorder.pop(0)
            root = TreeNode(root_val)

            mid = map_inorder[root_val]
            
            root.left = helper(l,mid-1)
            root.right = helper(mid+1,r)
            return root
        
        return helper(0,len(inorder)-1)
