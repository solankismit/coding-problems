"""
2101. Detonate the Maximum Bombs
Medium
1.6K
97
Companies
You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
"""
from collections import defaultdict


# import math
# class Solution(object):
#     def maximumDetonation(self, bombs):
#         """
#         :type bombs: List[List[int]]
#         :rtype: int
#         """
#
#     def distroy(self,bombs):
#         chances = dict()
#         for j in bombs:
#             chances.update({bombs.index(j) : []})
#             for i in bombs:
#                 distance = self.findDistance(j,i)
#                 if distance<=j[2]:
#                     chances[bombs.index(j)].append(i)
#         return chances
#     def findDistance(self,a,b):
#         return math.sqrt(math.pow((a[0]-b[0]),2)+math.pow((a[1]-b[1]),2))
#
#
# s1 = Solution()
# print(s1.distroy([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))

class Solution:
    def maximumDetonation(self, bombs):
        n, max_bombs, graph = len(bombs), 0, defaultdict(list)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if bombs[i][2] ** 2 >= (bombs[i][0] - bombs[j][0]) ** 2 + (bombs[i][1] - bombs[j][1]) ** 2:
                    graph[i] += [j]
            print(graph)

        def dfs(node, visited):
            for child in graph[node]:
                if child not in visited:
                    visited.add(child)
                    dfs(child, visited)

        for i in range(n):
            visited = {i}
            dfs(i, visited)
            max_bombs = max(max_bombs, len(visited))

        return max_bombs
s1 = Solution()
print(s1.maximumDetonation([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]))