class Solution:
    def minEatingSpeed(self, piles, h):
        import math
        
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            hours = sum(math.ceil(p / mid) for p in piles)
            
            if hours > h:
                left = mid + 1
            else:
                right = mid
        
        return left


# Example
piles = [3,6,7,11]
h = 8
print(Solution().minEatingSpeed(piles, h))