# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一
# 格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但
# 它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？ 
# 
#  
# 
#  示例 1： 
# 
#  输入：m = 2, n = 3, k = 1
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：m = 3, n = 1, k = 0
# 输出：1
#  
# 
#  提示： 
# 
#  
#  1 <= n,m <= 100 
#  0 <= k <= 20 
#  
#  Related Topics 深度优先搜索 广度优先搜索 动态规划 👍 432 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """

        def get_sum(num):
            digitSum = 0
            while num > 0:
                m = num % 10
                num = num // 10
                digitSum += m
            return digitSum

        def is_clear(cell):
            i, j = cell
            return marked[i][j] == 0

        def get_children(cell):
            i, j = cell
            return ((i + a, j + b)
                    for a in range(-1, 2)
                    for b in range(-1, 2)
                    if a == 0 or b == 0
                    if not (a == 0 and b == 0)
                    if 0 <= i + a < m
                    if 0 <= j + b < n
                    ## i 和 j一定要分清楚
                    if get_sum(i + a) + get_sum(j + b) <= k
                    if is_clear((i + a, j + b))
                    )

        def dfs(cell):
            i, j = cell
            marked[i][j] = 1
            self.res += 1
            for child in get_children(cell):
                dfs(child)

        marked = [[0] * n for _ in range(m)]
        self.res = 0
        dfs((0, 0))
        return self.res


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.movingCount(7, 2, 3)