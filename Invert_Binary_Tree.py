class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap left and right
        root.left, root.right = root.right, root.left
        
        # Recursively invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
