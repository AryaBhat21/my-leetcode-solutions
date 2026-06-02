class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        d  = {}
        n = len(nums)

        for i in nums:
            d[i] = d.get(i,0) + 1

        for i in d:
            if d[i]>(n//2):
                return i
        
        return -1