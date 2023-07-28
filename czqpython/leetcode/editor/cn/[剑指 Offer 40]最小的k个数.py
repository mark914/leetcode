# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#  
# 
#  示例 2： 
# 
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0] 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= k <= arr.length <= 10000 
#  0 <= arr[i] <= 10000 
#  
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 402 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        def patition(arr, l, r):
            if l > r: return -1
            x = arr[r]
            i = l - 1
            for j in range(l, r):
                if arr[j] <= x:
                    i += 1
                    arr[j], arr[i] = arr[i], arr[j]
            arr[i + 1], arr[r] = arr[r], arr[i + 1]
            return i + 1
        l, r = 0, len(arr) - 1
        while l < r:
            p = patition(arr, l, r)
            if p == k - 1:
                break
            elif p > k - 1:
                r = p - 1
            else:
                l = p + 1
        return arr[:k]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()