class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k = k1 + k2
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        
        if sum(diff) <= k:
            return 0
        
        diff.sort(reverse=True)
        n = len(diff)
        
        diff.append(0)
        
        for i in range(n):
            count = i + 1
            gap = diff[i] - diff[i + 1]
            needed = count * gap
            
            if k >= needed:
                k -= needed
            else:
                base_reduction = k // count
                extra = k % count
                target = diff[i] - base_reduction
                
                for j in range(count):
                    if j < extra:
                        diff[j] = target - 1
                    else:
                        diff[j] = target
                break
        
        return sum(diff[j] * diff[j] for j in range(n))