# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 双指针 排序 👍 4540 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def nSum(nums, target, n, start):
            res = []
            if n < 2: return res
            if n == 2:
                lo, hi = start, len(nums) - 1
                while lo < hi:
                    left, right = nums[lo], nums[hi]
                    total = left + right
                    if total > target:
                        while lo < hi and nums[hi] == right: hi -= 1
                    elif total < target:
                        while lo < hi and nums[lo] == left: lo += 1
                    else:
                        res.append([left, right])
                        while lo < hi and nums[hi] == right: hi -= 1
                        while lo < hi and nums[lo] == left: lo += 1
            else:
                i = 0
                while i < len(nums):
                    subs = nSum(nums, target-nums[i], n - 1, i + 1)
                    if subs:
                        for sub in subs:
                            sub.append(nums[i])
                            res.append(sub)
                    while i < len(nums) - 1 and nums[i] == nums[i + 1]: i += 1
                    i += 1
            return res
        nums.sort()
        return nSum(nums, 0, 3, 0)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.threeSum([-1,0,1,2,-1,-4])