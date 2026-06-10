class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n!=1 and n not in s:
            s.add(n)
            tot=0
            while n>0:
                d=n%10
                tot+=d*d
                n//=10
            n=tot
        return n==1
        