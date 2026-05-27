class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not self.isAlphaNumeric(s[l]):
                l += 1
            elif not self.isAlphaNumeric(s[r]):
                r -= 1
            elif s[l].upper() == s[r].upper():
                l += 1
                r -= 1
            else:
                return False

        return True
    
    def isAlphaNumeric(self, c):
        return c.isalnum()
        