from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        
        q = deque([root])
        res = []
        
        while q:
            n = len(q)
            
            for i in range(n):
                node = q.popleft()
                
                if i == n - 1:
                    res.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return res