from itertools import combinations
from math import sqrt

class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        
        def get_distance(lst):
            a, b = lst
            return sqrt((a[0] - b[0])** 2 + (a[1] - b[1])**2)
    
        def get_area(lst):
            a, b, c = lst
            
            if a <= 0 or b <= 0 or c <= 0:
                return 0
            
            if c >= a + b or a >= b + c or b >= a + c:
                return 0
            
            s = sum(lst) / 2
    
            # try:
            #     area = sqrt(s * (s - a) * (s - b) * (s - c))
            # except ValueError:
            #     print(s, [a, b, c], points)
            
            return area

        coord_list = list(combinations(points, 3))
        # print(coord_list)

        side_list = [list(map(get_distance, combinations(coords, 2))) for coords in coord_list]

        area_list = list(map(get_area, side_list))

        arg, mx = max(enumerate(area_list), key=lambda x: x[1])

        # print(arg)

        return mx