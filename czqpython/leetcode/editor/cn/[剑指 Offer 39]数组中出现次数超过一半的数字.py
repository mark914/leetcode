# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。 
# 
#  
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
# 输出: 2 
# 
#  
# 
#  限制： 
# 
#  1 <= 数组长度 <= 50000 
# 
#  
# 
#  注意：本题与主站 169 题相同：https://leetcode-cn.com/problems/majority-element/ 
# 
#  
#  Related Topics 数组 哈希表 分治 计数 排序 👍 264 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        votes = 0
        x = 0
        for num in nums:
            if votes == 0:
                x = num
            votes = votes + 1 if num == x else votes - 1
        return x
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()