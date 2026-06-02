class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sym = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        i=0
        ans=0
        
        while i<len(s):
            if i+1<len(s) and sym[s[i]]<sym[s[i+1]]:
                ans+=sym[s[i+1]]-sym[s[i]]
                i+=2
            else:
                ans+=sym[s[i]]
                i+=1
        return ans