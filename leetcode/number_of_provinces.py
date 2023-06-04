"""
547. Number of Provinces
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        d = {}
        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if i not in d.keys():
                    d[i] = []
                # if i == j:
                #     continue
                elif isConnected[i][j] == 1:
                    d[i].append(j)
                    # print(d)
        print(d)

        provinces=0
        visited = [] 
        for i in range(len(isConnected)):
            if i not in visited:
                provinces+=1
                self.dfs(i,d,visited)
        print(provinces)
        return provinces
    
    def dfs(self,i,d,visited):
        visited.append(i)
        for j in d[i]:
            if j not in visited:
                self.dfs(j,d,visited)
        return visited
    
    


        

s1 = Solution()
s1.findCircleNum([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]])
