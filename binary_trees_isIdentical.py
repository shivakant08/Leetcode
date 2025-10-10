class Solution:
    def isIdentical(r1, r2):
        if r1 is None and r2 is None:
            return True
        
        if r1 is None or r2 is None:
            return False

        if r1.data == r2.data:
            return self.isIdentical(r1.left, r2.left) and self.isIdentical(r1.right, r2.right)