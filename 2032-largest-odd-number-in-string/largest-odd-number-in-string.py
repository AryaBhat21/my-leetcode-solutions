class Solution:
    def largestOddNumber(self, num: str) -> str:
        end = -1
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2 == 1:
                end=i
                break
        i=0
        while i<=end and num[i]=="0":
            i+=1
        return num[i:end+1]
