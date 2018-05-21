class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--",
                 "-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letters = 'abcdefghijklmnopqrstuvwxyz'
        lookup_table = {letter: code for letter, code in zip(letters, codes)}
        
        def word_to_code(word):
            result = ''
            
            for char in word:
                result += lookup_table.get(char)
            
            return result
        
        return len(set(map(word_to_code, words)))