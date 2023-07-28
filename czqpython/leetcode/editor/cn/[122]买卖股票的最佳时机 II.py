# 给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。 
# 
#  在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。 
# 返回 你能获得的 最大 利润 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: prices = [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#  
# 
#  示例 2: 
# 
#  
# 输入: prices = [1,2,3,4,5]
# 输出: 4
# 解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
#      注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
#  
# 
#  示例 3: 
# 
#  
# 输入: prices = [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 3 * 10⁴ 
#  0 <= prices[i] <= 10⁴ 
#  
#  Related Topics 贪心 数组 动态规划 👍 1556 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ## dp[i][0] 表示持有股票， 可能是之前也在持有，可能是今天刚买（第一次买，买了之后再买）,要在之前买卖的理论的接触上来买股票
        ## dp[i][1] 表示未持有股票， 可能是之前就卖掉了，也可能是今天刚卖掉
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        dp[0] = [-prices[0], 0]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
        return dp[n-1][1]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()