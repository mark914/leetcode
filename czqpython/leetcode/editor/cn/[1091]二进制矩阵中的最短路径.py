# 给你一个 n x n 的二进制矩阵 grid 中，返回矩阵中最短 畅通路径 的长度。如果不存在这样的路径，返回 -1 。 
# 
#  二进制矩阵中的 畅通路径 是一条从 左上角 单元格（即，(0, 0)）到 右下角 单元格（即，(n - 1, n - 1)）的路径，该路径同时满足下述要求
# ： 
# 
#  
#  路径途经的所有单元格都的值都是 0 。 
#  路径中所有相邻的单元格应当在 8 个方向之一 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。 
#  
# 
#  畅通路径的长度 是该路径途经的单元格总数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [[0,1],[1,0]]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == grid.length 
#  n == grid[i].length 
#  1 <= n <= 100 
#  grid[i][j] 为 0 或 1 
#  
#  Related Topics 广度优先搜索 数组 矩阵 👍 163 👎 0

from collections import deque
# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # get children
        # every time step+ 1
        # when to stop
        n = len(grid)

        def is_clear(cell):
            """judge whether cell can reachable"""
            return grid[cell[0]][cell[1]] == 0

        def get_children(cell):
            i, j = cell
            res = (
                (i + a, j + b)
                for a in (-1, 0, 1)
                for b in (-1, 0, 1)
                if a != 0 or b != 0
                if 0 <= i + a < n
                if 0 <= j + b < n
                if is_clear((i + a, i + b))
            )
            return res

        start = (0, 0)
        goal = (n - 1, n - 1)
        queue = deque()
        if not is_clear(start) or not is_clear(goal):
            return -1
        queue.append(start)
        grid[0][0] = 1
        step = 1
        while queue:
            for _ in range(len(queue)):
                cell = queue.popleft()
                for child in get_children(cell):
                    grid[child[0]][child[1]] = 1
                    queue.append(child)

                if cell == goal: return step
            step += 1

        return -1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]])