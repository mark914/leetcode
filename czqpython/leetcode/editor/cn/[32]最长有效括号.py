# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 10⁴ 
#  s[i] 为 '(' 或 ')' 
#  
#  
#  
#  Related Topics 栈 字符串 动态规划 👍 1737 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxLength = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == '(': continue
            if s[i - 1] == '(':
                dp[i] = 2
                if i - 2 >= 0:
                    dp[i] += dp[i - 2]
            else:
                if dp[i - 1] == 0: continue
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] += dp[i - 1] + 2
                    if i - dp[i - 1] - 2 >= 0:
                        dp[i] += dp[i - dp[i - 1] - 2]
            maxLength = max(maxLength, dp[i])

        return maxLength
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.longestValidParentheses("))())()()())))")