class Solution:
    def reverseDegree(self, s: str) -> int:
        sum_rev = 0
        for i, val in enumerate(s, start=1):
            sum_rev += i*(ord('z')-ord(val)+1)
        return sum_rev
