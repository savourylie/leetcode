class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        sentence_list = S.split()
        
        def convert(word):
            vowels = 'aeiou'
            
            if word[0].lower() in vowels:
                return word + 'ma'
            else:
                return word[1:] + word[0] + 'ma'
            
        goat_latin_list = [convert(word) + 'a' * (i + 1) for i, word in enumerate(sentence_list)]
        
        return ' '.join(goat_latin_list)