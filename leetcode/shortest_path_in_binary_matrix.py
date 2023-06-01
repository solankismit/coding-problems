"""
1091. Shortest Path in Binary Matrix
Medium

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 """
from typing import List
from queue import Queue


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        n = len(grid)
        dx = [-1, 0, 1]
        dy = [-1, 0, 1]

        queue = Queue()
        queue.put([0, 0, 1])
        grid[0][0] = 1

        while not queue.empty():
            x, y, steps = queue.get()

            if x == n - 1 and y == n - 1:
                return steps

            for i in range(3):
                for j in range(3):
                    nx = x + dx[i]
                    ny = y + dy[j]

                    if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == 0:
                        queue.put([nx, ny, steps + 1])
                        grid[nx][ny] = 1

        return -1