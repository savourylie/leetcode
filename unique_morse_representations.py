class Solution(object):
    def __init__(self):
        morse_code_list = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                           "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        letter_list = list('abcdefghijklmnopqrstuvwxyz')

        self.letter_morse_dict = dict(zip(letter_list, morse_code_list))

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        num_morses = len(set(map(self._word_to_morse, words)))

        return num_morses

    def _word_to_morse(self, word):
        morse_code = [self.letter_morse_dict[char] for char in word]

        return ''.join(morse_code)
