class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        count_dict = {}
        para_list = paragraph.split()
        
        for word in para_list:
            lower_word = word.lower().strip(" !?',;.")
            if lower_word not in banned:
                count_dict[lower_word] = count_dict.get(lower_word, 0) + 1
                
        print(count_dict)
        
        return max(count_dict.items(), key=lambda x:x[1])[0]
            