class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        if n == 1:
            return nums[0]
        
        idx = n // 2
        idx_prev = idx - 1 if idx >= 1 else 0
        idx_next = idx + 1 if idx < n - 1 else n - 1
        
        if nums[idx_prev] != nums[idx] != nums[idx_next]:
            return nums[idx]
        
        if nums[idx] == nums[idx_next]:
            if len(nums[idx:]) % 2 == 0:
                return self.singleNonDuplicate(nums[:idx])
            else:
                return self.singleNonDuplicate(nums[idx:])                
        else:
            if len(nums[:idx_next]) % 2 == 0:
                return self.singleNonDuplicate(nums[idx_next:])
            else:
                return self.singleNonDuplicate(nums[:idx_next])