class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = 0
        for i in range(n):
            dist_ele = set()
            for j in range(i,n):
                dist_ele.add(nums[j])
                count = len(dist_ele)
                total_sum += count*count
        return total_sum