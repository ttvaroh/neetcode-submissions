class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = [ch.lower() for ch in s if ch.isalnum()]
        l = 0
        r = len(parsed)-1
        while l < r:
            if parsed[l] != parsed[r]:
                return False
            l+=1
            r-=1
        return True