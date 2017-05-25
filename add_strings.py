# Correct but TLE

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        return self.int_to_string(self.string_to_int(num1) + self.string_to_int(num2))


    def string_to_int(self, str_num):
        digit_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

        int_num = 0

        for i, x in enumerate(str_num):
            int_num += digit_dict[x] * 10 ** (len(str_num) - i - 1)

        return int_num

    def int_to_string(self, num):
        print(num)
        if num == 0:
            return '0'

        digit_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

        quo = num
        highest = 0

        while quo > 0:
            highest += 1
            quo, res = divmod(quo, 10)

        int_list = []
        quo = num

        while highest > 0:
            temp = quo
            quo, res = divmod(quo, 10**(highest - 1))
            int_list.append(quo)
            quo = temp - quo * 10**(highest - 1)
            highest -= 1


        print(int_list)
        list_str = list(map(digit_dict.get, int_list))

        return ''.join(list_str)
