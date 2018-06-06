class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.count = 0
        self.helper(N, list(range(1, N + 1)))
        
        return self.count
    
    def helper(self, N, n_list, b_index=1):
        if b_index > N:
            self.count += 1
            
        for x in n_list:
            if x % b_index == 0 or b_index % x == 0:
                n_list_copy = n_list[:]
                n_list_copy.remove(x)
                self.helper(N, n_list_copy, b_index + 1)