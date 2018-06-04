class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        queue = sorted(sorted(people, key=lambda x: x[1]), key=lambda x: x[0], reverse=True)
        result_list = []
        
        for x in queue:
            result_list.insert(x[1], x)
        
        return result_list