class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict()
        f = [[] for i in range(len(nums)+1)]

        for i in nums:
            if i in map:
                map[i] += 1
            else:
                map[i] = 1
        
        for num, cnt in map.items():
            f[cnt].append(num)
        
        res = []

        for i in range(len(f) - 1, 0, -1):
            for num in f[i]:
                res.append(num)
                if len(res) == k:
                    return res
        