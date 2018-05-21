class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        def letter_to_pos(letter):
            return ord(letter) - 97
        
        counter = 0
        width = 0
        
        for x in S:
            width += widths[letter_to_pos(x)]

            if width > 100:
                counter += 1
                width = widths[letter_to_pos(x)]
            
            elif width == 100:
                print(width)
                counter += 1
                width = 0
                
            else:
                pass

        if width != 0:
            counter += 1
                
        return [counter, width]