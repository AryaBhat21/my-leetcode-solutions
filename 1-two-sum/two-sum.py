class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        d = {}
        for i in range(len(nums)):
            num = nums[i]
            comp = target - num

            if comp in d:
                return [d[comp],i]

            d[num] = i