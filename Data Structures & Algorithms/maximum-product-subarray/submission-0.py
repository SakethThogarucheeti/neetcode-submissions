class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        currmin, currmax = 1,1

        for n in nums:
            tmp = currmax * n

            currmax = max(n * currmax, n * currmin, n)
            currmin = min(tmp, n * currmin, n)

            res = max(res, currmax)
        return res