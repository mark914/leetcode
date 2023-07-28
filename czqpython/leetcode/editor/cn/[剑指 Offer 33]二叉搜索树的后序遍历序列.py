# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。 
# 
#  
# 
#  参考以下这颗二叉搜索树： 
# 
#       5
#     / \
#    2   6
#   / \
#  1   3 
# 
#  示例 1： 
# 
#  输入: [1,6,3,2,5]
# 输出: false 
# 
#  示例 2： 
# 
#  输入: [1,3,2,6,5]
# 输出: true 
# 
#  
# 
#  提示： 
# 
#  
#  数组长度 <= 1000 
#  
#  Related Topics 栈 树 二叉搜索树 递归 二叉树 单调栈 👍 470 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """
        def recur(i, j):
            if i >= j:
                return True
            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            if p != j:
                return False
            return recur(i, m - 1) and recur(m, j - 1)
        return recur(0, len(postorder) - 1)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()