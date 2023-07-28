# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。 
# 
#  元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s 由 可打印的 ASCII 字符组成 
#  
#  Related Topics 双指针 字符串 👍 235 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        def isVowel(ch):
            return ch in "aeiouAEIOU"

        def swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        length = len(s)
        i = 0
        j = length - 1

        s = list(s)
        while i < j:
            while i < length and not isVowel(s[i]):
                i += 1
            while j >= 0 and not isVowel(s[j]):
                j -= 1

            if i < j:
                swap(s, i, j)
                i += 1
                j -= 1

        return "".join(s)

if __name__ == '__main__':
    s = Solution()
    s.reverseVowels('hello')

# leetcode submit region end(Prohibit modification and deletion)
