class Solution:
    def myPow(self, x: float, n: int) -> float:
        temp = n
        if n < 0:
            temp = -1*n
        ans =1.0000000000000000000

        while temp:
            if temp%2==0:
                x=x*x
                temp = temp/2
            else:
                ans=ans*x
                temp -= 1
        if n<0:
            ans = 1/ans

        return ans
