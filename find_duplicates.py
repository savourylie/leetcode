class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        result_list = []
        
        for x in nums:
            if nums[abs(x) -  1] < 0:
                result_list.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
                
        return result_list