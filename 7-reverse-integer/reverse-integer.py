class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x<0:
            neg = True
            x = x*(-1)
        temp = x
        val = 0
        while temp>0:
            rem = temp%10
            val = val*10 + rem
            temp = temp//10
        if neg:
            val = val*(-1)
        if x <= -(2**31) or x >=(2**31)-1 or val <= -(2**31) or val >=(2**31)-1:
            return 0
        return val