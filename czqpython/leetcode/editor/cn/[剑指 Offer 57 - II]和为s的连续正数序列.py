# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。 
# 
#  序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。 
# 
#  
# 
#  示例 1： 
# 
#  输入：target = 9
# 输出：[[2,3,4],[4,5]]
#  
# 
#  示例 2： 
# 
#  输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  
# 
#  
# 
#  限制： 
# 
#  
#  1 <= target <= 10^5 
#  
# 
#  
#  Related Topics 数学 双指针 枚举 👍 371 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        l = r = 1
        curSum = 0
        while l <= target // 2:
            if curSum < target:
                curSum += r
                r += 1
            elif curSum > target:
                curSum -= l
                l += 1
            else:
                arr = list(range(l, r))
                res.append(arr)
                curSum -= l
                l += 1
        return res



# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.findContinuousSequence(9)