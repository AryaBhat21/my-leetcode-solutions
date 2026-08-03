class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height)-1
        while left<right:
            ht = min(height[left],height[right])
            wd = right - left
            area = max(area, ht*wd)
            if height[left]<height[right]:
                left += 1
            else:
                right-=1
        return area