from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        f1 = defaultdict(int)
        tf1 = 0

        wf = defaultdict(int)
        twf = 0

        for i in range(len(s1)):
            curr1 = s1[i]
            f1[curr1] += 1
            tf1 += 1

            curr2 = s2[i]
            wf[curr2] += 1
        
        if f1 == wf:
            return True

        print(wf)
        s1len = len(s1)
        for r in range(len(s1), len(s2)):
            
            rch = s2[r]
            wf[rch] += 1
            
            l = r - len(s1)
            lch = s2[l]
            wf[lch] -= 1

            if wf[lch] == 0:
                wf.pop(lch)
            
            print(wf.items())

            if f1 == wf:
                return True
        
        return False


        