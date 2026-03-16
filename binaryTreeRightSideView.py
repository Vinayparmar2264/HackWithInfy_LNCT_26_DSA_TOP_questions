# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# method 1

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root :
            return []
        res = []
        level = 0

        def dfs(root,level):
            if not root :
                return 
            if len(res)==level:
                res.append(root.val)
            
            dfs(root.right,level+1)
            dfs(root.left,level+1)

        dfs(root,level)
        return res
            

# method 2

# from collections import deque
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # if not root:
        #     return []
        # my_dict = {}
        # queue = deque()
        # queue.append((0,root))
        
        # while queue:
        #     size = len(queue)
        #     for node in range(size):
        #         line, e = queue.popleft()
        #         my_dict[line] = e.val
        #         if e.left:
        #             queue.append((line+1,e.left))
        #         if e.right:
        #             queue.append((line+1,e.right))
        # result = [val for key,val in my_dict.items()]
        # return result

    
