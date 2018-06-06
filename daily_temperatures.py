class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        result_list = [0] * len(temperatures)
        stack = []
        
        for i, t in enumerate(temperatures):
            while stack:
                idx, temp = stack.pop()
                if t > temp:
                    result_list[idx] = i - idx
                else:
                    stack.append((idx, temp))
                    break
            stack.append((i, t))
            
        return result_list