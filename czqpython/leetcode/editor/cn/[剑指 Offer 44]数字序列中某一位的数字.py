# 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4，
# 等等。 
# 
#  请写一个函数，求任意第n位对应的数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：n = 3
# 输出：3
#  
# 
#  示例 2： 
# 
#  输入：n = 11
# 输出：0 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= n < 2^31 
#  
# 
#  注意：本题与主站 400 题相同：https://leetcode-cn.com/problems/nth-digit/ 
#  Related Topics 数学 二分查找 👍 196 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        ## 题目说实话是有点难的
        ## 不断从n中减去count，直到n <= count
        ## 此时的n就是在该digit下，从start到该位数的距离
        ## 此时可以用start + (n - 1)//digit得到num的大小
        ## 然后再用 (n-1) % digit 得到在num中的位数
        ## 最终得到该位数所对应的结果
        digit, start, count = 1, 1, 9
        while n > count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * digit * start
        num = start + (n - 1) // digit
        ## 得到某int中某一位数，先转化为str，使用切片，然后再转化为int
        return int(str(num)[(n - 1) % digit])

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()