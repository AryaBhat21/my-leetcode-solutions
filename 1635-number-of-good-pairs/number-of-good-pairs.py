class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d={}
        pair = 0

        for i in nums:
            d[i] = d.get(i,0)+1

        for i in d:
            if d[i] > 1:
                pair += ((d[i]-1)*d[i])//2

        return pair
        