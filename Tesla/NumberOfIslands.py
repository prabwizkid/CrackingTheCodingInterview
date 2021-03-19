# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1

# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3


class Graph:
    def __init__(self, row, col, g):
        self.row = row
        self.col = col
        self.g = g

    def dfs(self, i, j, visited):
        rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]
        colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]
        visited[i][j] = True

        for k in range(8):
            if (0 <= i < self.row and
                    0 <= j < self.col and
                    not visited[i][j] and self.g[i][j]):
                self.dfs(i + rowNbr[k], j + colNbr[k], visited)

    def islands(self):
        visited = [[False for j in range(self.col)] for i in range(self.row)]

        count = 0
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j] == False and self.g[i][j] == 1:
                    self.dfs(i, j, visited)
                    count += 1

        return count


graph = [[1, 1, 1, 1, 0],
         [1, 1, 0, 1, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0]]

row = len(graph)

col = len(graph[0])

g = Graph(row, col, graph)
print(g.islands())
