from collections import Counter


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        self.result_list = []

        _ = self.find_frequent_tree_sum(root)

        most_frequent_counter = Counter(self.result_list).most_common()
        max_num = most_frequent_counter[0][1]

        return [x for x, c in most_frequent_counter if c == max_num]

    def find_frequent_tree_sum(self, root):
        if not root:
            return 0

        tree_sum = root.val + self.find_frequent_tree_sum(root.left) + self.find_frequent_tree_sum(root.right)

        self.result_list.append(tree_sum)

        return tree_sum