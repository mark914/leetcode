# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
#  Related Topics 字符串 动态规划 👍 4724 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## res其实包含了最长所需要的要素（长度），因此不需要再用maxL进行记录
        def extendSub(start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1
            return s[start+1:end]


        res = ""
        for i in range(len(s)):
            sub1 = extendSub(i, i)
            sub2 = extendSub(i, i + 1)
            res = sub1 if len(res) < len(sub1) else res
            res = sub2 if len(res) < len(sub2) else res

        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()