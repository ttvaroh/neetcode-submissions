class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = [ch.lower() for ch in s if ch.isalnum()]
        l = 0
        r = len(parsed)-1
        while l < r:
            if (not parsed[l].isalnum()):
                l += 1
                continue
            if (not parsed[r].isalnum()):
                r -= 1
                continue
            if parsed[l].lower() != parsed[r].lower():
                return False
            l+=1
            r-=1
        return True