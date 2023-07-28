# 输入一个字符串，打印出该字符串中字符的所有排列。 
# 
#  
# 
#  你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。 
# 
#  
# 
#  示例: 
# 
#  输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#  
# 
#  
# 
#  限制： 
# 
#  1 <= s 的长度 <= 8 
#  Related Topics 字符串 回溯 👍 519 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        path = []
        s = sorted(s)
        used = [0] * len(s)
        def dfs():
            if len(path) == len(s):
                res.append(''.join(path))
                return
            for i in range(len(s)):
                if used[i]:
                    continue
                if i > 0 and s[i] == s[i - 1] and not used[i-1]:
                    continue
                path.append(s[i])
                used[i] = 1
                dfs()
                used[i] = 0
                path.pop()

        dfs()
        return res



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()