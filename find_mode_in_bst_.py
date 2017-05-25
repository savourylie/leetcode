# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.counter = {}

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)

        sorted_count = sorted(self.counter.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in sorted_count if x[1] == sorted_count[0][1]]

    def helper(self, root):
        if not root:
            return self.counter

        self.counter[root.val] = self.counter.get(root.val, 0) + 1
        self.counter.update(self.helper(root.left))
        self.counter.update(self.helper(root.right))

        return self.counter