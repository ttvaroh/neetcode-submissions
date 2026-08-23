class Solution:
    def maxArea(self, heights: List[int]) -> int:
        best = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l], heights[r]) * (r-l)
            best = max(best, area)
            if (heights[r] < heights[l]):
                r -= 1
            else:
                l += 1
        
        return best
