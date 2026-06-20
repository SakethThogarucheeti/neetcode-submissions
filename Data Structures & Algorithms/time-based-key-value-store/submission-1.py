class TimeMap:

    def __init__(self):
        self.times = {} # list of [val, ts]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = []
        self.times[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:

        res, values = "", self.times.get(key, [])
        length = len(values)
    
        l = 0
        r = length - 1
        print(l, r)
        while l <= r:
            mid = (l+r)//2

            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
