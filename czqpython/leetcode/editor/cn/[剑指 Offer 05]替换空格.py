# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
# 
#  
# 
#  示例 1： 
# 
#  输入：s = "We are happy."
# 输出："We%20are%20happy." 
# 
#  
# 
#  限制： 
# 
#  0 <= s 的长度 <= 10000 
#  Related Topics 字符串 👍 231 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for ss in s:
            if ss == " ":
                res.append("%20")
            else:
                res.append(ss)
        return "".join(res)


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()