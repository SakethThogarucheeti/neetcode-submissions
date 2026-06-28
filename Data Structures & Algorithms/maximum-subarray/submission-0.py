class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        submax = nums[0]

        for i in range(1, len(nums)):
            submax = max(nums[i], submax + nums[i])
            maxi = max(maxi, submax)
        return maxi