class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 0
        letters = {}
        l = 0
        currMax = 0
        for r in range(len(s)):
            letters[s[r]] = letters.get(s[r], 0) + 1
            currMax = max(letters.values())
            while r-l+1 > currMax + k:
                letters[s[l]] -= 1
                if letters[s[l]] == currMax-1:
                    currMax = max(letters.values())
                if letters[s[l]] == 0:
                    del letters[s[l]]
                l += 1
            best = max(best, r-l+1)
        return best
