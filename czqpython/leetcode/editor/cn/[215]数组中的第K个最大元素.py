# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 1463 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import random
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        k = len(nums) - k

        l, h = 0, len(nums) - 1
        # random.shuffle(nums)
        while l < h:
            j = self.partition(nums, l, h)
            if j == k:
                break
            elif j > k:
                h = j - 1
            else:
                l = j + 1

        return nums[k]

    def partition(self, nums, l, h):

        val = nums[h]
        i = l
        for j in range(l, h):
            if nums[j] <= val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[h] = nums[h], nums[i]

        return i
    # leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3,2,1,5,6,4] ,2))