# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O",
# "X","X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] 为 'X' 或 'O' 
#  
#  
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 719 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        def get_children(cell):
            i, j = cell
            return ((i + a, j + b)
                    for a in [-1, 0, 1]
                    for b in [-1, 0, 1]
                    if a == 0 or b == 0
                    if not (a == 0 and b == 0)
                    if 0 <= i + a < m
                    if 0 <= j + b < n
                    if is_O((i + a, j + b))
                    )

        def is_O(cell):
            i, j = cell
            return board[i][j] == 'O'

        def dfs(cell):
            if not is_O(cell):
                return
            i, j = cell
            board[i][j] = "T"
            for child in get_children(cell):
                dfs(child)

        for j in range(n):
            dfs((0, j))
            dfs((m - 1, j))
        for i in range(m):
            dfs((i, 0))
            dfs((i, n - 1))

        for i in range(m):
            for j in range(n):
                if board[i][j] == "T":
                    board[i][j] = "O"
                if board[i][j] == "O":
                    board[i][j] = "X"
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.solve([["O","O","O"],["O","O","O"],["O","O","O"]])