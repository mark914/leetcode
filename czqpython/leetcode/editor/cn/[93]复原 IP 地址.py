# 有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。 
# 
#  
#  例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 
# 和 "192.168@1.1" 是 无效 IP 地址。 
#  
# 
#  给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新
# 排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "25525511135"
# 输出：["255.255.11.135","255.255.111.35"]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "0000"
# 输出：["0.0.0.0"]
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "101023"
# 输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 20 
#  s 仅由数字组成 
#  
#  Related Topics 字符串 回溯 👍 795 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def isValid(start, end):
            if start > end: return False
            if s[start] == '0' and start != end: return False
            if not 0 <= int(s[start:end+1]) <=255: return False
            return True
        def dfs(startIndex):
            if len(s) > 12: return []
            if startIndex == len(s) and len(path) == 4:
                res.append(".".join(path))
                return
            if len(path) > 4: return
            for i in range(startIndex, len(s)):
                if not isValid(startIndex, i): break
                path.append(s[startIndex:i+1])
                dfs(i + 1)
                path.pop()

        res = []
        path = []
        dfs(0)
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()