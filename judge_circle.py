from collections import Counter

class Solution:
    # def __init__(self):
    #     self.move_dict = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        # position = [0, 0]
        #
        # for move in moves:
        #     u, v = self.move_dict[move]
        #
        #     position[0] += u
        #     position[1] += v
        #
        # return position == [0, 0]

        move_counter = Counter(moves)

        return move_counter['L'] == move_counter['R'] and move_counter['U'] == move_counter['D']
