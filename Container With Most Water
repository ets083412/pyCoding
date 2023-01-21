class Solution(object):
    def maxArea(self, height):
        max_container = 0
        for p1 in range(len(height)):
            for p2 in range(p1+1,len(height)):
                heights = min(height[p1],height[p2])
                width = p2 - p1
                container = heights * width
                max_container = max(max_container, container)
        return max_container
