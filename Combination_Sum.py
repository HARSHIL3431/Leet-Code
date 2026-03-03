class Solution:
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # reuse allowed
                path.pop()

        backtrack(0, [], 0)
        return res


# Example
sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))