class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower()
        l = 0
        r = len(s1) - 1
        while l < r:
            if not s1[l].isalnum():
                l += 1
            elif not s1[r].isalnum():
                r -= 1
            elif s1[l] == s1[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
