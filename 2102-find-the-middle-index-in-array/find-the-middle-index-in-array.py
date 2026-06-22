class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            right_sum = tot_sum - left_sum - num 

            if left_sum == right_sum:
                return i
            
            left_sum += num

        return -1
        