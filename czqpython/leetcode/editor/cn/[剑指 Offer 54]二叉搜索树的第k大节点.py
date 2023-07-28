# 给定一棵二叉搜索树，请找出其中第 k 大的节点的值。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: root = [3,1,4,null,2], k = 1
#    3
#   / \
#  1   4
#   \
#    2
# 输出: 4 
# 
#  示例 2: 
# 
#  
# 输入: root = [5,3,6,2,4,null,null,1], k = 3
#        5
#       / \
#      3   6
#     / \
#    2   4
#   /
#  1
# 输出: 4 
# 
#  
# 
#  限制： 
# 
#  
#  1 ≤ k ≤ 二叉搜索树元素个数 
#  
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 270 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.idx = 0
        self.res = None
        def traverse(node):
            if not node: return
            traverse(node.right)
            self.idx += 1
            if self.idx == k:
                self.res = node
                return
            traverse(node.left)
        traverse(root)
        return self.res.val

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()