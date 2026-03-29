# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,max_so_far):
            count = 0
            if not root:
                return 0

            if max_so_far <= root.val:
                count = 1
                max_so_far = root.val

            
            count += dfs(root.left,max_so_far)
            count += dfs(root.right,max_so_far)
            return count
        
        return dfs(root, root.val)