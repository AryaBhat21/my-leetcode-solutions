class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums = sorted(nums)
        n = len(nums)
        lastsmall = float("-inf")
        longest = 1
        count = 0

        for i in range(n):
            if nums[i]-1 == lastsmall:
                count += 1
                lastsmall = nums[i]

            elif lastsmall != nums[i]:
                count = 1
                lastsmall = nums[i]

            longest = max(longest, count)

        return longest

