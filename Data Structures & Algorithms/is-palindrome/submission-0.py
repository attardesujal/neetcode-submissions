class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(c for c in s if c.isalnum())
        s=s.lower()
        reversed_s=s[::-1]
        if s == reversed_s:
            return True
        else:
            return False
        