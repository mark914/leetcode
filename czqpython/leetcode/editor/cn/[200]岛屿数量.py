# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 1529 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        def get_chilren(cell):
            i, j = cell
            return ((i + a, j + a)
                    for a in [-1, 0, 1]
                    for b in [-1, 0, 1]
                    if a == 0 or b == 0
                    if not (a == 0 and b == 0)
                    if 0 <= i + a < m
                    if 0 <= j + b < n
                    if is_land((i + a, j + b))
                    )

        def is_land(cell):
            i, j = cell
            return grid[i][j] == "1"

        def dfs(cell):
            if not is_land(cell):
                return
            i, j = cell
            grid[i][j] = "0"
            for child in get_chilren(cell):
                dfs(child)

        sumLand = 0
        for i in range(m):
            for j in range(n):
                cell = (i, j)
                if is_land(cell):
                    dfs(cell)
                    sumLand += 1

        return sumLand


# leetcode submit region end(Prohibit modification and deletion)



if __name__ == "__main__":
    s = Solution()
    s.numIslands([ ["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"] ])