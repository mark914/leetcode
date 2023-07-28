# 给定一个整数数组 prices ，它的第 i 个元素 prices[i] 是一支给定的股票在第 i 天的价格。 
# 
#  设计一个算法来计算你所能获取的最大利润。你最多可以完成 k 笔交易。 
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。 
# 
#  示例 2： 
# 
#  
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7
# 解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
#      随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 
# 。 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= k <= 100 
#  0 <= prices.length <= 1000 
#  0 <= prices[i] <= 1000 
#  
#  Related Topics 数组 动态规划 👍 666 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """

        ## 最多进行k次交易，那一共有2*k + 1种状态,奇数为买入状态，偶数为卖出状态
        ## 买入状态， dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] - prices[i])
        ## 卖出状态： dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + prices[i])
        ## 注意考虑len(prices)为0的情况
        n = len(prices)
        if n==0: return 0
        dp = [[0] * (2*k + 1) for _ in range(n)]
        dp[0] = [0 if i % 2 == 0 else -prices[0] for i in range(2*k + 1)]

        for i in range(1, n):
            for j in range(0, 2*k, 2):
                dp[i][j+1] = max(dp[i-1][j+1], dp[i-1][j] - prices[i])
                dp[i][j+2] = max(dp[i-1][j+2], dp[i-1][j+1] + prices[i])

        return dp[n-1][2*k]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()