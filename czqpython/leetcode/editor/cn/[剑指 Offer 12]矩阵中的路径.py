# 给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  例如，在下面的 3×4 的矩阵中包含单词 "ABCCED"（单词中的字母已标出）。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = 
# "ABCCED"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["a","b"],["c","d"]], word = "abcd"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  board 和 word 仅由大小写英文字母组成 
#  
# 
#  
# 
#  注意：本题与主站 79 题相同：https://leetcode-cn.com/problems/word-search/ 
#  Related Topics 数组 回溯 矩阵 👍 548 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def is_clear(cell):
            i, j = cell
            return marked[i][j] == 0
        def get_children(cell):
            i, j = cell
            return ((i + a, j + b)
                    for a in range(-1, 2)
                    for b in range(-1, 2)
                    if not (a == 0 and b == 0)
                    if a != 0 or b != 0
                    if 0 <= i + a < m
                    if 0 <= j + b < n
                    if is_clear((i+a, j+b))
                    )
        m, n = len(board), len(board[0])
        marked = [[0] * n for _ in range(m)]
        def dfs(cell, index):
            i, j = cell
            if board[i][j] != word[index]:
                return False
            if index >= len(word) - 1:
                return True
            marked[i][j] = 1
            for child in get_children(cell):
                a, b = child
                if board[a][b] != word[index + 1]: continue
                if dfs(child, index + 1):
                    return True
            marked[i][j] = 0
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs((i, j), 0):
                        return True


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    # board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    # word = "ABCCED"
    # s.exist(board, word)