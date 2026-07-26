class Solution:
    def maxProduct(self, n: int) -> int:
        temp = n
        ans=[]
        while temp>0:
            ans.append(temp%10)
            temp=temp//10
        ans.sort()
        return ans[-1]*ans[-2]