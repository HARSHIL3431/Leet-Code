class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        
        res = ""
        
        for i in range(len(s)):
            # odd length
            temp = expand(i, i)
            if len(temp) > len(res):
                res = temp
            
            # even length
            temp = expand(i, i+1)
            if len(temp) > len(res):
                res = temp
        
        return res