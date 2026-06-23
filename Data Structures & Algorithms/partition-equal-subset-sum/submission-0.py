class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        
        if total % 2 == 1:
            return False
        
        dp = set()
        dp.add(0)
        target = total/2 
        for i in nums:
            newsums = set()
            for s in dp:
                if s + i == target:
                    return True
                newsums.add(s + i)
            dp = dp.union(newsums)
        
        
        if target in dp:
            return True
        else:
            return False
        