# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
#  Related Topics 数组 矩阵 模拟 👍 354 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res

        rowBegin = 0
        rowEnd = len(matrix) - 1
        colBegin = 0
        colEnd = len(matrix[0]) - 1
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # towards right
            for i in range(colBegin, colEnd + 1):
                res.append(matrix[rowBegin][i])
            rowBegin += 1

            # toward down
            for i in range(rowBegin, rowEnd + 1):
                res.append(matrix[i][colEnd])
            colEnd -= 1

            # toward left
            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    res.append(matrix[rowEnd][i])
            rowEnd -= 1

            # toward up
            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    res.append(matrix[i][colBegin])
            colBegin += 1

        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])