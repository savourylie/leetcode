from itertools import product

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        str_list = list(S)
        combine_list = []
        
        for x in str_list:
            if x.islower():
                temp_list = [x, x.upper()]
            elif x.isupper():
                temp_list = [x, x.lower()]
            else:
                temp_list = [x]
            
            combine_list.append(temp_list)
            
        
        return [''.join(tup) for tup in product(*combine_list)]