# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。 
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。 
# 
#  注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/ 
#  Related Topics 队列 滑动窗口 单调队列 堆（优先队列） 👍 412 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        queue = deque()
        if len(nums) == 0 or k == 0:
            return []
        for i in range(k):
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
        res.append(queue[0])
        for i in range(k, len(nums)):
            if nums[i - k] == queue[0]:
                queue.popleft()
            while queue and queue[-1] < nums[i]:
                queue.pop()
            queue.append(nums[i])
            res.append(queue[0])
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()