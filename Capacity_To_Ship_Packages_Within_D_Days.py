class Solution:
    def shipWithinDays(self, weights, days):
        left, right = max(weights), sum(weights)
        
        while left < right:
            mid = (left + right) // 2
            required_days = 1
            curr_weight = 0
            
            for w in weights:
                if curr_weight + w > mid:
                    required_days += 1
                    curr_weight = 0
                curr_weight += w
            
            if required_days > days:
                left = mid + 1
            else:
                right = mid
        
        return left


# Example
weights = [1,2,3,4,5,6,7,8,9,10]
days = 5
print(Solution().shipWithinDays(weights, days))