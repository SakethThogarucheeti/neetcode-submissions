class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1]
        right = [1]

        for i in nums:
            if not left:
                left.append(i)
                continue
            left.append(left[-1]*i)
        
        for i in range(len(nums)-1, -1, -1):
            print(i)
            if not right:
                right.append(nums[i])
                continue
            right.append(right[-1]*nums[i])
        
        right.reverse()

        print(left, right)

        res = []

        for i in range(len(nums)):
            res.append(left[i]* right[i+1])
        return res