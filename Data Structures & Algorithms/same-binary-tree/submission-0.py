class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # Case 1: both nodes are None
        if not p and not q:
            return True
        
        # Case 2: one is None, other is not
        if not p or not q:
            return False
        
        # Case 3: values are different
        if p.val != q.val:
            return False
        
        # Case 4: values same → check left and right subtree
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        
        return left and right