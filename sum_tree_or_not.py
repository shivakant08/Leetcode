# Helper Function
class Solution:
    def calcSum(self, root):
        if root is None:
            return 0
        
        return self.calcSum(root.left) + self.calcSum(root.right) + root.data

    def is_sum_tree(self, root):
        if root is None or (root.left is None and root.right is None):
            retuurn True
        
        if self.is_sum_tree(root.left) and self.is_sum_tree(root.right):
            left_sum = self.calcSum(root.left)
            right_sum = self.calcSum(root.right)

            return root.data = left_sum + right_sum
        return False