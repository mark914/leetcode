# 给定两个整数数组，preorder 和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵
# 树的后序遍历，重构并返回二叉树。 
# 
#  如果存在多个答案，您可以返回其中 任何 一个。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：preorder = [1,2,4,5,3,6,7], postorder = [4,5,2,6,7,3,1]
# 输出：[1,2,3,4,5,6,7]
#  
# 
#  示例 2: 
# 
#  
# 输入: preorder = [1], postorder = [1]
# 输出: [1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= preorder.length <= 30 
#  1 <= preorder[i] <= preorder.length 
#  preorder 中所有值都 不同 
#  postorder.length == preorder.length 
#  1 <= postorder[i] <= postorder.length 
#  postorder 中所有值都 不同 
#  保证 preorder 和 postorder 是同一棵二叉树的前序遍历和后序遍历 
#  
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 230 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        """
        :type preorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(preorder, preStart, preEnd, \
                   postorder, postStart, postEnd):
            if preStart > preEnd: return None
            if preStart == preEnd: return TreeNode(preorder[preStart])
            rootVal = preorder[preStart]
            leftVal = preorder[preStart + 1]
            idx = hashMap.get(leftVal)
            leftSize = idx - postStart + 1
            root = TreeNode(rootVal)
            root.left = helper(preorder, preStart + 1, preStart + leftSize, \
                               postorder, postStart, idx)
            root.right = helper(preorder, preStart+leftSize+1, preEnd, \
                                postorder, idx+1, postEnd-1)
            return root
        hashMap = {}
        for i, x in enumerate(postorder):
            hashMap[x] = i
        n = len(preorder)
        return helper(preorder, 0, n-1,\
                      postorder, 0, n-1)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()