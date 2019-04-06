class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result_list = []

        for word in words:
            match_tuples = zip(word, pattern)
            first_second_dict = {}
            second_first_dict = {}

            for tup in match_tuples:
                first, second = tup

                if second not in second_first_dict and first not in first_second_dict:
                    second_first_dict[second] = first
                    first_second_dict[first] = second

                else:
                    try:
                        first_temp = second_first_dict[second]
                    except KeyError:
                        pass
                    else:
                        if first_temp != first:
                            break

                    try:
                        second_temp = first_second_dict[first]
                    except KeyError:
                        pass
                    else:
                        if second_temp != second:
                            break
            else:
                result_list.append(word)

        return result_list


if __name__ == '__main__':
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    pattern = "abb"

    s = Solution()
    print(s.findAndReplacePattern(words, pattern))
