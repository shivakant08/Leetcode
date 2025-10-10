class Solution:
    def isMirror(self, p, q):
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        return p.val == q.val and self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left)



    def isSymmetric(self, root):
        if not root:
            return True
        
        return self.isMirror(root.left, root.right3)
