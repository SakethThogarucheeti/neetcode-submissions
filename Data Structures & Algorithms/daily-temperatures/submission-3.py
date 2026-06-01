#20:07
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        res = [0] * len(temperatures)
        for tidx, t in enumerate(temperatures):
            print(tidx, t)
            print(stack, res)
            if len(stack) == 0:
                stack.append([t,tidx])
                continue
            while stack:
                top = stack[-1]
                print("considering , ", top)
                res[top[1]] = tidx - top[1]
                top = stack[-1]
                if top[0] < t:
                    top = stack.pop()
                else:
                    break
            stack.append([t,tidx])
        
        while stack:
            top = stack.pop()
            res[top[1]] = 0

        return res
