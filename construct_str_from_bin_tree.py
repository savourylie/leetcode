class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        
        if t is None:
            return ''
        
        def tree2str_sub(t):
            if t is None:
                return '()'

            left = tree2str_sub(t.left)
            right = tree2str_sub(t.right)
            
            if left == '()':
                if right == '()':
                    combined = ''
                else:
                    combined = '()' + '(' + right + ')'
            else:
                if right == '()':
                    combined = '(' + left + ')'
                else:
                    combined = '(' + left + ')' + '(' + right + ')'
                    
            sub = str(t.val) + combined

            return sub
        
        result = tree2str_sub(t)
            
        return result