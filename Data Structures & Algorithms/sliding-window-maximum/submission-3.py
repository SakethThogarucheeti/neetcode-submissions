from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1 3 2 1 0 0 1 2
        # store the max 
        # store the second largest
        # when the max goes out of the window, then the max becomes the second largest in the window
        # when the window leaves an element, it should be removed from the maxi storage
        # so we will need to store k elements and remove one element every time. 
        # the removed element should have an index lesser than l
        # the next max should be calculated
        # what data structure allows us to store k elements, let's us remove elements based on index in O(1) or o(logn) 
        # and let's us query the next max
        # heapq with (value, key)?
        # when the window moves a step, we pop until heapq[0]'s key is larger than l
        # get the largest element and add it to res 

        q = deque()
        l = r = 0
        res = []
        
        while r < len(nums):
            if q and l > q[0][0]:
                q.popleft()
            while q and q[-1][1] < nums[r]:
                q.pop()
            q.append((r, nums[r]))
            
            
            if (r + 1) >= k:
                res.append(q[0][1])
                l+=1
            r+=1
            
        return res
        