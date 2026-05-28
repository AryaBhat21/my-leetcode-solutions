class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        maximum = 0
        counter = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                if counter > maximum : 
                    maximum = counter

            else:
                counter = 0

        return maximum

        