# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# method 1
# class Solution:
    # def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
    #     elif not p and q or not q and p:
    #         return False
    #     queue = deque()
    #     if p.val == q.val:
    #         queue.append((p,q))
    

    #     while queue:
    #         ep , eq = queue.popleft()
            
    #         if ep.val != eq.val:
    #             return False
            
    #         else:
    #             if ep.left and eq.left:
    #                     queue.append((ep.left,eq.left))
    #             elif ep.left and not eq.left or not ep.left and eq.left:
    #                 return False
    #             if ep.right and eq.right:
    #                     queue.append((ep.right,eq.right))
    #             elif ep.right and not eq.right or not ep.right and eq.right:
    #                 return False

    #     return True

# method 2

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q :
            return False

        if p.val != q.val:
            return False
        return  self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
    

        
