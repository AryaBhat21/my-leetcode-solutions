class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        i=n
        while True:
            temp = i
            val = 1
            while temp>0:
                rem = temp%10
                val = val*rem
                temp = temp//10
            if val%t==0:
                return i
            i+=1