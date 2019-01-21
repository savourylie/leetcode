class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        self._insert(root, val)

        return root

    def _insert(self, current, val):
        if val > current.val:
            if current.right is not None:
                self._insert(current.right, val)
            else:
                current.right = TreeNode(val)
        else:
            if current.left is not None:
                self._insert(current.left, val)
            else:
                current.left = TreeNode(val)
