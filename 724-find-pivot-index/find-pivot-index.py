class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        left_sum = 0
        right_sum = 0

        for i, v in enumerate(nums):
            right_sum = tot_sum - left_sum - v

            if left_sum == right_sum:
                return i
            
            left_sum += v

        return -1
                


        

