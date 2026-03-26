class Solution:
    def restoreIpAddresses(self, s: str):
        res = []

        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            for l in range(1, 4):
                if start + l > len(s):
                    break

                part = s[start:start+l]

                if (part[0] == '0' and l > 1) or int(part) > 255:
                    continue

                path.append(part)
                backtrack(start + l, path)
                path.pop()

        backtrack(0, [])
        return res