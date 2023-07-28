# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == matrix.length 
#  n == matrix[i].length 
#  1 <= m, n <= 10 
#  -100 <= matrix[i][j] <= 100 
#  
#  Related Topics 数组 矩阵 模拟 👍 982 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m, n = len(matrix), len(matrix[0])
        startRow = 0
        endRow = m - 1
        startCol = 0
        endCol = n - 1
        ans = []
        while len(ans) < m * n:

            for i in range(startCol, endCol + 1):
                if len(ans) < m * n:
                    ans.append(matrix[startRow][i])
            startRow += 1

            for i in range(startRow, endRow):
                if len(ans) < m * n:
                    ans.append(matrix[i][endCol])
            endCol -= 1

            for i in range(endCol, startCol - 1, -1):
                if len(ans) < m * n:
                    ans.append(matrix[endRow][i])
            endRow -= 1

            for i in range(endRow, startRow - 1, -1):
                if len(ans) < m * n:
                    ans.append(matrix[i][startCol])
            startCol += 1

        return ans
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])