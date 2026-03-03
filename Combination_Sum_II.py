class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])  # no reuse
                path.pop()

        backtrack(0, [], 0)
        return res


# Example
sol = Solution()
print(sol.combinationSum2([10,1,2,7,6,1,5], 8))