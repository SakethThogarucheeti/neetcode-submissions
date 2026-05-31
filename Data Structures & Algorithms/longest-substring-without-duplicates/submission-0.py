class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ls = dict()
        l = 0
        r = 0
        res = 0
        while r < len(s):
            print(l,r,ls)
            curr = s[r]

            if curr in ls:
                lsc = ls[curr]
                ls[curr] = r
                if lsc >= l:
                    res = max(res, r-l)
                    l = lsc+1
            else:
                ls[curr] = r
            r+= 1
        print(l,r,ls)
        return max(res, r-l)



        