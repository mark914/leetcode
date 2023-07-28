# 找出数组中重复的数字。 
# 
#  
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
# 找出数组中任意一个重复的数字。 
# 
#  示例 1： 
# 
#  输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3 
#  
# 
#  
# 
#  限制： 
# 
#  2 <= n <= 100000 
#  Related Topics 数组 哈希表 排序 👍 690 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums):
            if i == nums[i]:
                i += 1
            else:
                if nums[i] ==  nums[nums[i]]:
                    return nums[i]
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        return -1
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3])