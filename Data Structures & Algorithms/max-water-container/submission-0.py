class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def calc(left, lh, right, rh):
            return min(lh, rh) * abs(left - right)
        
        left = 0
        right = len(heights) - 1

        maxi = 0
        while left < right:
            curr = calc(left, heights[left], right, heights[right])
            maxi = max(maxi, curr)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxi
        