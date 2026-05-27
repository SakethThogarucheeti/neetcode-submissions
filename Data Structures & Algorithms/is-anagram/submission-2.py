class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sarr = list(s)
        tarr = list(t)
        print(sarr)

        sarr.sort()
        tarr.sort()
        print(sarr)

        for i in range(len(s)):
            if sarr[i] != tarr[i]:
                return False
        
        return True

        