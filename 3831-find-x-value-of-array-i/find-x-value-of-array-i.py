class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        ans = [0] * k
        dp = [0] * k

        for x in nums:
            v = x % k
            next_dp = [0] * k
            
            # Subarray consisting solely of nums[i]
            next_dp[v] += 1
            
            # Extend subarrays ending at nums[i - 1]
            for r in range(k):
                if dp[r] > 0:
                    next_dp[(r * v) % k] += dp[r]
            
            # Accumulate to global count
            for r in range(k):
                ans[r] += next_dp[r]
            
            dp = next_dp

        return ans