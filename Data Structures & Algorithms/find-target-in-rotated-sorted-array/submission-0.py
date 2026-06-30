class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        
        piv = l

        l = 0
        r = len(nums) - 1

        if target >= nums[piv] and target <= nums[r]:
            l = piv
        else:
            r = piv - 1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1

        