# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level_sum = 0
            size = len(queue)
            for _ in range(size):
                e = queue.popleft()
                level_sum += e.val
                if e.left:
                    queue.append(e.left)
                if e.right:
                    queue.append(e.right)
            res.append(level_sum/size)
        
        return res
