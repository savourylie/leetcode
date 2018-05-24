class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
    
        def flood_fill(image, sr, sc, new_color, old_color):
            color = image[sr][sc]
            
            if color != old_color:
                return None
            
            M = len(image)
            N = len(image[0])
            
            neighbors = [(sr + x, sc) for x in {-1, 1} if 0 <= sr + x < M] \
            + [(sr, sc + x) for x in {-1, 1} if 0 <= sc + x < N]
            
            if color == old_color:
                image[sr][sc] = new_color
            
            for neigh in neighbors:
                flood_fill(image, neigh[0], neigh[1], new_color, old_color)
                
            return None
        
        _ = flood_fill(image, sr, sc, newColor, old_color)
        
        return image
                
            
            