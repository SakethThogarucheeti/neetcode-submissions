class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for s in strs:
            sarr = list(s)
            sarr.sort()
            skey = "".join(sarr)
            if skey in map:
                map[skey].append(s)
            else:
                map[skey] = [s]
        
        print(map)
        res = []
        for key in map:
            res.append(map[key])

        return res