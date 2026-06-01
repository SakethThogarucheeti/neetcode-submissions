class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) 
        

        while l < r:
            mid = (l + r)//2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return -1

        