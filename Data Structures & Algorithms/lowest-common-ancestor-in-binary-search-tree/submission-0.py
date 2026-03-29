class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        # Both nodes are in left subtree
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)

        # Both nodes are in right subtree
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)

        # Split point — this is the LCA
        return root