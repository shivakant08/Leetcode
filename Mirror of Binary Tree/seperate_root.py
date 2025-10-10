class Solution:
    def is isMirror(self, r1, r2):
        if not r1 and not r2:
            return True

        if not r1 or not r2:
            return False
        
        return r1.val == r2.val and self.isMirror(r1.left, r2.right) and self.isMirror(r1.right, r2.left)