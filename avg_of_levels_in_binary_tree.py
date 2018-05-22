# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        global result_dict
        result_dict = defaultdict(list)
        
        def dfs(root, level=0):
            if not root:
                return None
            
            global result_dict
            result_dict[level].append(root.val)
            
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)
            
        _ = dfs(root)
        
        len_arr = len(result_dict)
        
        result_list = [None] * len_arr
        
        for key, val in result_dict.items():
            result_list[key] = sum(result_dict[key]) / len(result_dict[key])
            
        return result_list