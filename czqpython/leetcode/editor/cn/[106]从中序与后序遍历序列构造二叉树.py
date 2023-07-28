# 给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并
# 返回这颗 二叉树 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
# 输出：[3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# 输入：inorder = [-1], postorder = [-1]
# 输出：[-1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= inorder.length <= 3000 
#  postorder.length == inorder.length 
#  -3000 <= inorder[i], postorder[i] <= 3000 
#  inorder 和 postorder 都由 不同 的值组成 
#  postorder 中每一个值都在 inorder 中 
#  inorder 保证是树的中序遍历 
#  postorder 保证是树的后序遍历 
#  
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 691 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(postorder, p_start, p_end, \
                   inorder, i_start, i_end):
            if p_start > p_end: return None
            root = TreeNode(postorder[p_end])
            idx = hashMap.get(postorder[p_end])
            length_left = idx - i_start
            root.left = helper(postorder, p_start, p_start+length_left-1, \
                               inorder, i_start, idx-1)
            root.right = helper(postorder, p_start+length_left, p_end-1, \
                                inorder, idx + 1, i_end)
            return root

        hashMap = {}
        for i, x in enumerate(inorder):
            hashMap[x] = i
        n = len(postorder)
        return helper(postorder, 0, n-1, \
                      inorder, 0, n-1)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()