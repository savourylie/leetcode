class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        index = list(range(len(deck)))
        index_scrambled = self._scamble_index(index)

        index_ordered = [None] * len(deck)

        for i in index:
            pos = index_scrambled[i]
            index_ordered[pos] = i

        deck_sorted = sorted(deck)

        deck_ordered = [None] * len(deck)

        for i in range(len(deck)):
            deck_ordered[i] = deck_sorted[index_ordered[i]]

        return deck_ordered

    @staticmethod
    def _scamble_index(index):
        index = index[:]
        counter = 0
        result_list = []

        while index:
            element = index.pop(0)
            if counter % 2 == 0:
                result_list.append(element)
            else:
                index.append(element)

            counter += 1

        return result_list


if __name__ == '__main__':
    nums = [17,13,11,2,3,5,7]

    s = Solution()
    print(s.deckRevealedIncreasing(nums))