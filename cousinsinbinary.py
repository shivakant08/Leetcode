class Solution:
    def isCousin(self,root, x, y):
        if not root or x == y:
            return False

        q = deque([root])

        while q:
            s = len(q)
            x_found = False
            y_found = False

            for _ in range(s):
                current = q.popleft()
                if current.left and current.right:
                    if current.left.val == x and current.right.val == y or current.left.val == y and current.right.val == x:
                        return False

                if current.left:
                    q.append(current.left)
                    if current.left.val == x:
                        x_found = True
                    if current.left.val == y:
                        y_found = True

                if current.right:
                    q.append(current.right)
                    if current.right.val == x:
                        x_found = True
                    if current.right.val == y:
                        y_found = True
            if x_found and y_found:
                return True

            if x_found or y_found:
                return False
        return False


 
