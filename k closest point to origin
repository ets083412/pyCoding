class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def sortKey(e):
            return sqrt(e[0]**2 + e[1]**2)
        points.sort(key=sortKey)
        return points[:k]
