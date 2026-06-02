import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def timeTaken(speed):
            t = 0
            for p in piles:
                t += math.ceil(p/speed)
            return t


        maxp = max(piles)

        l = 1
        r = maxp
        
        speed = 0
        while l <= r:
            mid = (l + r)//2
            midtime = timeTaken(mid)

            print(l,r,midtime)
            if midtime <= h:
                speed = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return speed
        
