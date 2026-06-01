class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        sum_n = n*(n+1)//2
        mis_n_sum = 0

        for i in nums:
            mis_n_sum += i
        
        return sum_n - mis_n_sum
            

            
        