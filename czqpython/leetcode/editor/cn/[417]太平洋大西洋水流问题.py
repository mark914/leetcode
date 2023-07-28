# 给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。 
# 
#  规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。 
# 
#  请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。 
# 
#  
# 
#  提示： 
# 
#  
#  输出坐标的顺序不重要 
#  m 和 n 都小于150 
#  
# 
#  
# 
#  示例： 
# 
#  
# 
#  
# 给定下面的 5x5 矩阵:
# 
#   太平洋 ~   ~   ~   ~   ~ 
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * 大西洋
# 
# 返回:
# 
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
#  
# 
#  
#  Related Topics 深度优先搜索 广度优先搜索 数组 矩阵 👍 328 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(heights)
        n = len(heights[0])
        at = [[0] * n for _ in range(m)]
        pa = [[0] * n for _ in range(m)]

        ##转化为从两个大洋的边界能够到达的所有地方的交集
        def get_children(cell, reached):
            i, j = cell
            return ((i + a, j + b)
                    for a in [-1, 0, 1]
                    for b in [-1, 0, 1]
                    if a == 0 or b == 0
                    if not (a == 0 and b == 0)
                    if 0 <= i + a < m
                    if 0 <= j + b < n
                    if canReach((i + a, j + b), reached)
                    if heights[i][j] <= heights[i + a][j + b]
                    )

        def canReach(cell, reached):
            i, j = cell
            return reached[i][j] == 0

        def dfs(cell, reached):
            if not canReach(cell, reached):
                return
            i, j = cell
            reached[i][j] = 1
            for child in get_children(cell, reached):
                dfs(child, reached)

        for i in range(m):
            dfs((i, 0), pa)
            dfs((i, n - 1), at)

        for j in range(n):
            dfs((0, j), pa)
            dfs((m - 1, j), at)

        ans = []
        for i in range(m):
            for j in range(n):
                if pa[i][j] == 1 and at[i][j] == 1:
                    ans.append([i, j])

        return ans


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]])