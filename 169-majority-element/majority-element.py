class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        count = 0
        maj = 0
    
        uni = list(dict.fromkeys(nums))
        for i in uni:
            if nums.count(i)>count:
                count = nums.count(i)
                maj = i

        return maj

