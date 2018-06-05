# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        this_level = [root]
        temp_list = []
        result_list = []
        
        while this_level:
            next_level = []
            for x in this_level:
                if x is not None:
                    temp_list.append(x.val)
                    if x.left is not None:
                        next_level.append(x.left)            
                    if x.right is not None:
                        next_level.append(x.right)
            result_list.append(max(temp_list))
            temp_list = []
            this_level = next_level
            
        return result_list
                