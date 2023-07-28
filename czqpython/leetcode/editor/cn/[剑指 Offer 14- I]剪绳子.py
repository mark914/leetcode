# 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
# 请问 k[0]*k[1]*...*k[m-1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18
# 。 
# 
#  示例 1： 
# 
#  输入: 2
# 输出: 1
# 解释: 2 = 1 + 1, 1 × 1 = 1 
# 
#  示例 2: 
# 
#  输入: 10
# 输出: 36
# 解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36 
# 
#  提示： 
# 
#  
#  2 <= n <= 58 
#  
# 
#  注意：本题与主站 343 题相同：https://leetcode-cn.com/problems/integer-break/ 
#  Related Topics 数学 动态规划 👍 390 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## 应该用dp来做
        ## dp[i]表示长度为i的绳子的最大乘积
        ## dp[i] = max(dp[i], max(dp[i - j]*j, (i - j) * j))
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], max(dp[i - j] * j, (i - j) * j))
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()