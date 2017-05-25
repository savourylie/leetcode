from itertools import combinations, product

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        
        if num == 0:
            return ['0:00']
            
        combi = []
        
        for x in range(num + 1):
            combi.append(((num - x), x))
    
        combi = [x for x in combi if x[0] < 4 and x[1] < 6]
        
        result = []
        for x in combi:
            result.extend([y[0] + y[1] for y in product(self._n_to_hours(x[0]), self._n_to_mins(x[1]))])
            
        return result
        
        
    def _n_to_hours(self, n):
        """
        n in range(0, 4)
        """
    
        zeros = ['0:']
        ones = [str(2 ** x) + ':' for x in range(0, 4)]
        two_c = list(combinations([2 ** x for x in range(0, 4)], 2))
        twos = list(set([str(sum(x)) + ':' for x in two_c if str(sum(x)) + ':' not in ones and sum(x) < 12]))
        threes = list(set([str(sum(x)) + ':' for x in
                  product([2 ** x for x in range(0, 4)], [sum(x) for x in two_c if sum(x) not in ones]) if str(sum(x)) + ':' not in ones and str(sum(x)) + ':' not in twos and sum(x) < 12]))
    
        light_dict = dict()
        light_dict[0] = zeros
        light_dict[1] = ones
        light_dict[2] = twos
        light_dict[3] = threes
    
        return light_dict[n]
        
    def _n_to_mins(self, n):
        """
        n in range(0, 6)
        """
    
        zeros = ['00']
        ones = [2 ** x for x in range(0, 6)]
        two_c = list(combinations([2 ** x for x in range(0, 6)], 2))
        twos = list(set([sum(x) for x in two_c if sum(x) not in ones and sum(x) < 60]))
        threes = list(set([sum(x) for x in product(ones, twos) if sum(x) not in ones and sum(x) not in twos and sum(x) < 60]))
        fours = list(set([sum(x) for x in product(ones, threes) if sum(x) not in ones and sum(x) not in twos and sum(x) not in threes and sum(x) < 60]))
        fives = list(set([sum(x) for x in product(ones, fours) if sum(x) not in ones and sum(x) not in twos and sum(x) not in threes and sum(x) not in fours and sum(x) < 60]))
    
        light_dict = dict()
        light_dict[0] = zeros
        light_dict[1] = ['0' + str(x) if len(str(x)) == 1 else str(x) for x in ones]
        light_dict[2] = ['0' + str(x) if len(str(x)) == 1 else str(x) for x in twos]
        light_dict[3] = ['0' + str(x) if len(str(x)) == 1 else str(x) for x in threes]
        light_dict[4] = ['0' + str(x) if len(str(x)) == 1 else str(x) for x in fours]
        light_dict[5] = ['0' + str(x) if len(str(x)) == 1 else str(x) for x in fives]
    
        return light_dict[n]