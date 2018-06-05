class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        table = [[False for x in range(N)] for y in range(N)]
        count = 0
        
        # All singletons are palindromes
        for i in range(N):
            table[i][i] = True
            count += 1
            
        # Mark for length-two elements
        for i in range(N - 1):
            if s[i] == s[i+1]:
                table[i][i+1] = True
                count += 1
                
                
        # Mark for length-three and more
        for k in range(3, N + 1):
            for i in range(N - k + 1):
                if s[i] == s[i+k-1] and table[i+1][i+k-2] == True:
                    table[i][i+k-1] = True
                    count += 1
                    
        return count
            
        
        
        
#         N = len(s)        
#         result_list = []
        
#         for i in range(1, N + 1):
#             for j in range(0, N):
#                 if s[j:j+i] == s[j:j+i][::-1] and len(s[j:j+i]) == i:
#                     result_list.append(s[j:j+i])
        
#         # print(result_list)
        
#         return len(result_list)