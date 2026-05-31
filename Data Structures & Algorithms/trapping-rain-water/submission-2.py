class Solution:
    def trap(self, height: List[int]) -> int:
        from collections import deque
        prefixmax = deque()
        suffixmax = deque()

        for i in range(len(height)):
            last = prefixmax[-1] if len(prefixmax)>0 else 0
            currmax = max(height[i], last)
            prefixmax.append(currmax)
        
        for i in range(len(height) - 1, -1, -1):
            last = suffixmax[0] if len(suffixmax)>0 else 0
            currmax = max(height[i], last)
            suffixmax.appendleft(currmax)
        
        print(prefixmax, suffixmax)

        total = 0

        for hidx, h in enumerate(height):
            total += min(prefixmax[hidx], suffixmax[hidx]) - h
        print(total)

        return total







        