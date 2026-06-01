class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """

        change_5=0
        change_10=0
        change_20=0

        for i in range(len(bills)):
            if bills[i]==5:
                change_5+=1

            elif bills[i]==10:
                if change_5>0:
                    change_5-=1
                    change_10+=1
                else:
                    return False
            else:
                if change_5>0 and change_10>0:
                    change_5 -= 1
                    change_10 -= 1
                    change_20 += 1
                elif change_5>=3:
                    change_5 -= 3
                    change_20 += 1

                else:
                    return False

        return True     