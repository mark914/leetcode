# 给你一个整数数组 nums 和一个整数 target 。 
# 
#  向数组中的每个整数前添加 '+' 或 '-' ，然后串联起所有整数，可以构造一个 表达式 ： 
# 
#  
#  例如，nums = [2, 1] ，可以在 2 之前添加 '+' ，在 1 之前添加 '-' ，然后串联起来得到表达式 "+2-1" 。 
#  
# 
#  返回可以通过上述方法构造的、运算结果等于 target 的不同 表达式 的数目。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,1,1], target = 3
# 输出：5
# 解释：一共有 5 种方法让最终目标和为 3 。
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], target = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 20 
#  0 <= nums[i] <= 1000 
#  0 <= sum(nums[i]) <= 1000 
#  -1000 <= target <= 1000 
#  
#  Related Topics 数组 动态规划 回溯 👍 1047 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ## 可以看做是从组合中找到和为一定的子集
        total = sum(nums)
        if abs(target) > total: return 0
        if (total + target) & 1: return 0
        target = (total + target) // 2
        res = []
        path = []
        def dfs(startIndex, curSum):

            if target == curSum:
                res.append(path[:])

            for i in range(startIndex, len(nums)):
                # if i > startIndex and nums[i] == nums[i - 1]:
                #     continue
                if curSum + nums[i] > target: continue
                path.append(nums[i])
                curSum += nums[i]
                dfs(i + 1, curSum)
                curSum -= nums[i]
                path.pop()
        nums.sort()
        dfs(0, 0)
        return len(res)
# leetcode submit region end(Prohibit modification and deletion)



if __name__ == "__main__":
    s = Solution()
    s.findTargetSumWays([1, 1, 1, 1, 1], 3)