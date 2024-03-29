# 给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,5,11,5]
# 输出：true
# 解释：数组可以分割成 [1, 5, 5] 和 [11] 。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,3,5]
# 输出：false
# 解释：数组不能分割成两个元素和相等的子集。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
#  Related Topics 数组 动态规划 👍 1133 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total & 1: return False
        target = total // 2
        dp = [0] * (target + 1)
        ## 相当于向容量为target的背包里放物品，物品大小为w，价值也为w，因为物品总大小一定小于等于target
        ## 所以物品总价值也是一定小于等于target
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])

        return dp[target] == target

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()