class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()
        for idx, val in enumerate(nums):
            if target - val in map:
                return [map[target-val], idx]
            map[val] = idx            
        return False


        