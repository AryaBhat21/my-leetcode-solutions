class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        temp = x
        val = 0
        while temp>0:
            rem = temp%10
            val = val*10 + rem
            temp = temp//10
        print(val)
        if val == x:
            return True
        return False
