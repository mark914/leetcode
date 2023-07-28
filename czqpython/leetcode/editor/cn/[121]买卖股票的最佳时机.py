# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。 
# 
#  你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。 
# 
#  返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[7,1,5,3,6,4]
# 输出：5
# 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
#  
# 
#  示例 2： 
# 
#  
# 输入：prices = [7,6,4,3,1]
# 输出：0
# 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 10⁵ 
#  0 <= prices[i] <= 10⁴ 
#  
#  Related Topics 数组 动态规划 👍 2122 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## dp[i][0]持有股票的最大金钱 dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
        ## dp[i][1]不持有股票的最大金钱 dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        dp = [[0] * 2 for _ in range(len(prices)) ]
        dp[0][0], dp[0][1] = -prices[0], 0
        for i in range(1, len(prices)):
            ## 持有时候，要不是原来就持有，要么就是第一次买。也就是比较之前买入时花的钱数和现在的买需要的钱数进行对比
            dp[i][0] = max(dp[i - 1][0], - prices[i])
            ## 未持有的时候，要不就是之前就买了，要不就是现在买。也就是比较现在买划算，还是之前买划算
            dp[i][1] = max(dp[i - 1][1], dp[i-1][0] + prices[i])
        return dp[len(prices) - 1][1]




# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()