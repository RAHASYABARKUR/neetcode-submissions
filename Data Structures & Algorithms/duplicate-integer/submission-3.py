class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set(nums)
        print(list(seen))
        if len(list(seen)) != len(nums):
            return True
        else:
            return False
