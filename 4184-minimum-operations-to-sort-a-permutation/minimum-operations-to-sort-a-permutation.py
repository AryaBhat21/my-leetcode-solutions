class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        is_inc = True
        is_dec = True

        for i in range(n):
            nxt = (i + 1) % n
            if (nums[nxt] - nums[i]) % n != 1:
                is_inc = False
            if (nums[i] - nums[nxt]) % n != 1:
                is_dec = False

        if not is_inc and not is_dec:
            return -1

        idx = nums.index(0)

        if is_inc:
            ans = min(idx, (n - idx) % n + 2 if idx != 0 else 0)
            return ans

        if is_dec:
            cost1 = 1 + (n - 1 - idx)
            cost2 = ((idx + 1) % n) + 1

            return min(cost1, cost2)