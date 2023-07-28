# 统计一个数字在排序数组中出现的次数。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2 
# 
#  示例 2: 
# 
#  
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: 0 
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
# 
#  
# 
#  注意：本题与主站 34 题相同（仅返回值不同）：https://leetcode-cn.com/problems/find-first-and-last-
# position-of-element-in-sorted-array/ 
#  Related Topics 数组 二分查找 👍 288 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def getLeft(nums, target):
            l, r = 0, len(nums) - 1
            if target > nums[-1]: return -1
            while l < r:
                mid = l + (r - l) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l if nums[l] == target else -1

        def getRight(nums, target):
            l, r = 0, len(nums) - 1
            while l < r:
                mid = l + (r - l + 1) // 2
                if nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid
            return l
        if len(nums) == 0: return 0
        left = getLeft(nums, target)
        if left == -1:
            return 0
        right = getRight(nums, target)
        return right - left + 1

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()