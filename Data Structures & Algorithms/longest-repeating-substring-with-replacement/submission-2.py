class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0

        l = 0
        count = dict()
        maxf = 0
        for r in range(len(s)):
            curr = s[r]
            count[curr] = 1 + count.get(curr, 0)
            
            currfreq = count.get(curr)
            
            maxf = max(maxf, currfreq)
            
            winsize = r - l + 1
            
            countofotherchars = winsize - maxf
            
            while countofotherchars > k and l < r:
                lastchar = s[l]
                count[lastchar] -= 1
                countofotherchars -=1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res



        