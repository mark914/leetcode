# 给你一个正整数 n ，生成一个包含 1 到 n² 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
#  Related Topics 数组 矩阵 模拟 👍 593 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for _ in range(n)]
        startRow, endRow = 0, n - 1
        startCol, endCol = 0, n - 1
        k = 1
        while k <= n * n:
            for i in range(startCol, endCol + 1):
                if k <= n * n:
                    matrix[startRow][i] = k
                    k += 1
            startRow += 1

            for i in range(startRow, endRow + 1):
                if k <= n * n:
                    matrix[i][endCol] = k
                    k += 1
            endCol -= 1

            for i in range(endCol, startCol - 1, -1):
                if k <= n * n:
                    matrix[endRow][i] = k
                    k += 1
            endRow -= 1

            for i in range(endRow, startRow - 1, -1):
                if k <= n * n:
                    matrix[i][startCol] = k
                    k += 1
            startCol -= 1
        return matrix
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.generateMatrix(3)