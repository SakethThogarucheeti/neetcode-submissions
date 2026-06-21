class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            d1 = 0
            d2 = 0
            for i in range(len(nums)):
                curr = max(nums[i] + d2, d1)
                d2 = d1
                d1 = curr
            return max(d1, d2)
        return max(helper(nums[1:]), helper(nums[:-1]), nums[0] )
        