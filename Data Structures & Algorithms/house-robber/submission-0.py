class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = [-1] * len(nums)

        def dfs(i):
            if i>= len(nums):
                return 0
            if mem[i]!=-1:
                return mem[i]
            #mem[i] = cost[i] + max(dfs(i),dfs(i+2))
            mem[i] = max(nums[i]+dfs(i+2),dfs(i+1))
            return mem[i]
        
        return max(dfs(0),dfs(1))
        