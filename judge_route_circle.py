class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        lookup_table = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        move_incrementals = []
        result_pos = [0, 0]
        
        for i, x in enumerate(moves):
            move_incrementals.append(lookup_table.get(x))
            
        for x, y in move_incrementals:
            result_pos[0], result_pos[1] = result_pos[0] + x, result_pos[1] + y
            
        return True if sum(result_pos) == 0 else False