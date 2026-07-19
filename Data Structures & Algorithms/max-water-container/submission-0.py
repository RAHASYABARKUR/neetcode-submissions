class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        l,r = 0, len(heights) - 1

        while l<r:
            area = max((r-l)* min(heights[l],heights[r]),area)
            if heights[l] < heights[r]:
                l = l+1
            elif heights[r]<=heights[l]:
                r=r-1
        return area
        