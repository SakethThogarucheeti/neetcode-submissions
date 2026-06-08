class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, total):
            if total == target:
                res.append(subset)
                return

            if i == len(nums):
                return

            curr = subset
            curr_total = total

            while curr_total <= target:
                dfs(i + 1, curr, curr_total)

                curr = curr + [nums[i]]
                curr_total += nums[i]

        dfs(0, [], 0)
        return res