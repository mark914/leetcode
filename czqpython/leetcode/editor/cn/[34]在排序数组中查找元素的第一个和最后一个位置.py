# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
# 
#  如果数组中不存在目标值 target，返回 [-1, -1]。 
# 
#  进阶： 
# 
#  
#  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1] 
# 
#  示例 3： 
# 
#  
# 输入：nums = [], target = 0
# 输出：[-1,-1] 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 10⁵ 
#  -10⁹ <= nums[i] <= 10⁹ 
#  nums 是一个非递减数组 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics 数组 二分查找 👍 1420 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def getFirst(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        def getLast(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l + 1) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid
            return l
        if len(nums) == 0:
            return [-1, -1]
        left = getFirst(nums, target)
        if nums[left] != target:
            return [-1, -1]
        right = getLast(nums, target)
        return [left, right]








if __name__ == "__main__":
    a= Solution()
    a.searchRange([5,7,7,8,8,10], 4)


# leetcode submit region end(Prohibit modification and deletion)
