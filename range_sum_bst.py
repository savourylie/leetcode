class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        if not root:
            return None

        queue = [root]

        while queue:
            current = queue.pop(0)
            current_val = current.val

            if L <= current_val:
                if current_val <= R:
                    self.sum += current_val

                    if current.left:
                        queue.append(current.left)

                    if current.right:
                        queue.append(current.right)
                else:
                    if current.left:
                        queue.append(current.left)
            else:
                if current.right:
                    queue.append(current.right)

        return self.sum


if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left, root.left.right = TreeNode(3), TreeNode(7)
    root.right.left, root.right.right = None, TreeNode(18)

    L, R = 7, 15

    s = Solution()

    assert s.rangeSumBST(root, L, R) == 32
