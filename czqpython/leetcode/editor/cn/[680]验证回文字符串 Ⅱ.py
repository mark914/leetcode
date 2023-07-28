# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "aba"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abca"
# 输出: true
# 解释: 你可以删除c字符。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abc"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 由小写英文字母组成 
#  
#  Related Topics 贪心 双指针 字符串 👍 444 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[::-1] == s:
            return True
        l = 0
        r = len(s) - 1
        s = list(s)
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                a = s[l:r]
                b = s[l+1:r+1]
                return a[::-1] == a or b[::-1] == b


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()