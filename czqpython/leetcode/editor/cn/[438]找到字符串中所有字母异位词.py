# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。 
# 
#  异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length, p.length <= 3 * 10⁴ 
#  s 和 p 仅包含小写字母 
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 770 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ## 为求所有解的问题，这时候每个循环只需要对left向右移动一次
        ## 寻找子串排列时，窗口的长度是固定的，right向右得到的并不是一个可行解，
        ## 而是一个长度和len(p)相等的可能解，然后就判断这个可能解是否为解，
        ## 如果是解，那就添加到结果中，如果不是，说明以该left为起点的解不存在，left向右移动。
        need, window = {}, {}
        for ch in p:
            need[ch] = need.get(ch, 0) + 1
        valid = 0
        left = right = 0
        res = []
        while right < len(s):
            c = s[right]
            right += 1
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            while valid == len(need) and right - left >= len(p):
                if right - left == len(p):
                    res.append(left)
                d = s[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.findAnagrams("cbaebabacd", "abc")