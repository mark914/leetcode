# 给定一个字符串 s 和一个整数 k，从字符串开头算起，每计数至 2k 个字符，就反转这 2k 字符中的前 k 个字符。 
# 
#  
#  如果剩余字符少于 k 个，则将剩余字符全部反转。 
#  如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abcdefg", k = 2
# 输出："bacdfeg"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abcd", k = 2
# 输出："bacd"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 10⁴ 
#  s 仅由小写英文组成 
#  1 <= k <= 10⁴ 
#  
#  Related Topics 双指针 字符串 👍 274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s.strip()
        nums = list(s)
        n = len(nums)
        l, r = 0, 0
        while r < n:
            for _ in range(2 * k):
                if r < n: r += 1
            if r - l < k: r1 = r - 1
            l1, r1 = l, l + k - 1
            while l1 < r1:
                nums[l1], nums[r1] = nums[r1], nums[l1]
                l1 += 1
                r1 -= 1
            l = r
        return ''.join(nums)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.reverseStr("abcdefg", 3)
