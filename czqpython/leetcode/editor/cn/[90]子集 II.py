# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  
#  
#  Related Topics 位运算 数组 回溯 👍 735 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        subset = []
        def dfs(startIndex):
            res.append(subset[:])
            if startIndex == len(nums):
                return
            ## 同一枝干不能用同一位置上的元素，已经被startIndex完成了。
            uset = [0] * 21
            for i in range(startIndex, len(nums)):
                ## 同一层不能用值相同的元素
                if uset[nums[i] + 10]: continue
                uset[nums[i] + 10] = 1
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
        dfs(0)
        return res


        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()