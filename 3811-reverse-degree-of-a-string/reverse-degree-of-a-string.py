class Solution:
    def reverseDegree(self, s: str) -> int:
        s = s.lower()
        sum_rev = 0
        for i, val in enumerate(s, start=1):
            ind_rev = ord('z')-ord(val)+1
            sum_rev += ind_rev*i
        return sum_rev
