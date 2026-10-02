class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        sum_div = 1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                if i*i==num:
                    sum_div+=i
                else:
                    sum_div+=i+ (num//i)
        
        return num==sum_div
