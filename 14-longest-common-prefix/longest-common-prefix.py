class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        strs.sort()
        s1 = strs[0]
        s2 = strs[-1]
        i = 0
        while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
            i+=1
        return s1[:i]