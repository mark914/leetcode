# 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。 
# 
#  
# 
#  示例 1： 
# 
#  输入：nums = [4,1,4,6]
# 输出：[1,6] 或 [6,1]
#  
# 
#  示例 2： 
# 
#  输入：nums = [1,2,10,4,1,4,3,3]
# 输出：[2,10] 或 [10,2] 
# 
#  
# 
#  限制： 
# 
#  
#  2 <= nums.length <= 10000 
#  
# 
#  
#  Related Topics 位运算 数组 👍 587 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        diff = 0
        for num in nums:
            diff ^= num
        m = 1
        while diff & m == 0:
            m <<= 1
        res = [0] * 2
        for num in nums:
            if num & m: res[0] ^= num
            else: res[1] ^= num
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()