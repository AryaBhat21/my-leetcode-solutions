class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d = {}
        for i in t:
            d[i] = d.get(i,0)+1
        for j in s:
            d[j]-=1
        for i in d:
            if d[i]==1:
                return i

        return -1







        
        