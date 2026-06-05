class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d={}
        res=[]
        for i in nums:
            d[i] = d.get(i,0)+1

        
        while k>0:
            freq = 0
            ele = 0
            for i in d:
                if d[i]>freq:
                    freq = d[i]
                    ele = i
            res.append(ele)
            d[ele]=0
            k-=1
        
        return res

             

        