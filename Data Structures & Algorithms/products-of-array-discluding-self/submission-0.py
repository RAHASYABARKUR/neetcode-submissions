class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1]* (len(nums))

        for i in range(1,len(nums)):
            op[i] = op[i-1]*nums[i-1]
        pf = 1
        for i in range(len(nums)-1,-1,-1):
            op[i] = op[i]*pf
            pf=pf*nums[i]
        return op


        