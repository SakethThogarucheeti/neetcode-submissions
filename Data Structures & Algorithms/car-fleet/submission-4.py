from collections import defaultdict
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = []
        for i in range(len(position)):
            time = (target - position[i])/speed[i]
            car.append([position[i], speed[i], time])
        
        car.sort(reverse=True)
        print(car)
        s = []
        for i in range(len(car)):
            s.append(car[i])
            if len(s)>=2 and s[-1][2] <= s[-2][2]:
                s.pop()
            



        return len(s)
        