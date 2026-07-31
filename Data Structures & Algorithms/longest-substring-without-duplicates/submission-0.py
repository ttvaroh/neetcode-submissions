class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        hmap = {}  

        l = 0
        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r],0) + 1
            while hmap[s[r]] > 1:
                hmap[s[l]] -= 1
                l += 1
            best = max(best, r-l+1)
        return best