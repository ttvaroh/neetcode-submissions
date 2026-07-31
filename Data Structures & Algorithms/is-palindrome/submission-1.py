class Solution:
    def isPalindrome(self, s: str) -> bool:
        regular = ""
        reverse = ""

        for c in s:
            if c.isalnum():
                reverse = c.lower() + reverse
                regular += c.lower()
        
        if regular == reverse:
            return True
        return False