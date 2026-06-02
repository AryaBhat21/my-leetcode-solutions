class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        count = 0
        maj = None

        for i in nums:
            if count == 0:
                maj = i
            if i == maj:
                count+=1
            else:
                count -=1

        return maj

