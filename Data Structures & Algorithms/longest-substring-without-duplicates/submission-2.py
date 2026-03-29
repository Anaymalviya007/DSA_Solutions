class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxCount = 0
        L = 0 
        seen  = set()
        for R in range(len(s)):
            while s[R] in seen:
                seen.remove(s[L])
                L +=1
            
            seen.add(s[R])
            maxCount = max(maxCount, R - L + 1)
        return maxCount