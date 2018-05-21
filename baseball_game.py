class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        scores = []
        
        for op in ops:
            if op == '+':
                score = scores[-1] + scores[-2]
                scores.append(score)
            elif op == 'D':
                score = 2 * scores[-1]
                scores.append(score)
            elif op == 'C':
                scores.pop()
            else:
                try:
                    score = int(op)
                except ValueError:
                    raise ValueError("Invalid operation.")
                else:
                    scores.append(score)
            
        return sum(scores)