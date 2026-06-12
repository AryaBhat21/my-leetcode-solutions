class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c+=1
                res = max(res,c)

            else:
                c = 0
        return res

        