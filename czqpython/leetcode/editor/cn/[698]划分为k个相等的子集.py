# 给定一个整数数组 nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# 输出： True
# 说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。 
# 
#  示例 2: 
# 
#  
# 输入: nums = [1,2,3,4], k = 3
# 输出: false 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= len(nums) <= 16 
#  0 < nums[i] < 10000 
#  每个元素的频率在 [1,4] 范围内 
#  
#  Related Topics 位运算 记忆化搜索 数组 动态规划 回溯 状态压缩 👍 501 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartitionKSubsets(self, nums, k):
        target, m = divmod(sum(nums), k)
        if m: return False
        n = len(nums)
        dp = [0] * k
        res = None
        nums.sort(reverse=True)

        def dfs(i, res):
            if i == n:
                res = dp[:]
                return
            for j in range(k):
                dp[j] += nums[i]
                if dp[j] <= target :
                    dfs(i + 1)
                dp[j] -= nums[i]
                if not dp[j]: break
        if nums[0] > target: return False
        dfs(0, res)
        if len(set(res)) == 1: return True
        return False

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.canPartitionKSubsets([4,3,2,3,5,2,1], 4)