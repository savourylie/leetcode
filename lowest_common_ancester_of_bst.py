# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    candidate_queue = []
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        match = []
        queue = [root]
        
        while len(queue) != 0:
            current = queue.pop(0)
        
            if current:
                if current is p:
                    match.append(p)
                if current is q:
                    match.append(q)
                
                queue.append(current.left)
                queue.append(current.right)
        
        if len(match) == 2:
            self.candidate_queue.append(root)
        
        if root:            
            self.lowestCommonAncestor(root.left, p, q)
            self.lowestCommonAncestor(root.right, p, q)
            
        return self.candidate_queue[-1]