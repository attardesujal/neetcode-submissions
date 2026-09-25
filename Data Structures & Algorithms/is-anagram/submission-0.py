class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_t = "".join(sorted(t))
        sorted_s = "".join(sorted(s))
        if sorted_s == sorted_t:
            return True
        else:
            return False
        