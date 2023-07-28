# 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
#  
# 
#  如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  1 <= dictionary.length <= 1000 
#  1 <= dictionary[i].length <= 1000 
#  s 和 dictionary[i] 仅由小写英文字母组成 
#  
#  Related Topics 数组 双指针 字符串 排序 👍 286 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findLongestWord(self, s, dictionary):
        """
        1. 判断t是否为s子序列
        2. 维护一个长度最长，字典序最小的子序列

        :type s: str
        :type dictionary: List[str]
        :rtype: str
        """
        def isSubSequence(s, t):
            i = 0
            j = 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == len(t)

        res = ""
        for t in dictionary:
            if isSubSequence(s, t):
                if len(t) > len(res) or (len(t) == len(res) and t < res):
                    res = t

        return res




# leetcode submit region end(Prohibit modification and deletion)
