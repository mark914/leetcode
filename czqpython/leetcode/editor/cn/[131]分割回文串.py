# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  回文串 是正着读和反着读都一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 回溯 👍 981 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []
        def isPalindrome(start, end):
            temp = s[start:end+1]
            return temp == temp[::-1]
        def dfs(startIndex):
            if startIndex == len(s):
                res.append(path[:])
                return
            for i in range(startIndex, len(s)):
                if not isPalindrome(startIndex, i): continue
                path.append(s[startIndex:i+1])
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()