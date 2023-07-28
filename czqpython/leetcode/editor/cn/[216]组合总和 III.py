# 找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。 
# 
#  说明： 
# 
#  
#  所有数字都是正整数。 
#  解集不能包含重复的组合。 
#  
# 
#  示例 1: 
# 
#  输入: k = 3, n = 7
# 输出: [[1,2,4]]
#  
# 
#  示例 2: 
# 
#  输入: k = 3, n = 9
# 输出: [[1,2,6], [1,3,5], [2,3,4]]
#  
#  Related Topics 数组 回溯 👍 421 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        combination = []
        def dfs(startIndex, curSum):
            if curSum > n:
                return
            if k == len(combination):
                if curSum == n:
                    res.append(combination[:])
                    return
            for i in range(startIndex, 9 - (k - len(combination)) + 2):
                if curSum + i > n: continue
                combination.append(i)
                curSum += i
                dfs(i+1, curSum)
                curSum -= i
                combination.pop()
        dfs(1, 0)
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()