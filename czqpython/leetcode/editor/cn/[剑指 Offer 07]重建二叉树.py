# 输入某二叉树的前序遍历和中序遍历的结果，请构建该二叉树并返回其根节点。 
# 
#  假设输入的前序遍历和中序遍历的结果中都不含重复的数字。 
# 
#  
# 
#  示例 1: 
# 
#  
# Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
# Output: [3,9,20,null,null,15,7]
#  
# 
#  示例 2: 
# 
#  
# Input: preorder = [-1], inorder = [-1]
# Output: [-1]
#  
# 
#  
# 
#  限制： 
# 
#  0 <= 节点个数 <= 5000 
# 
#  
# 
#  注意：本题与主站 105 题重复：https://leetcode-cn.com/problems/construct-binary-tree-from-
# preorder-and-inorder-traversal/ 
#  Related Topics 树 数组 哈希表 分治 二叉树 👍 704 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        ## pre root left right
        ## ino left root right
        def buildTree_helper(preorder, p_start, p_end, \
                      inorder, i_start, i_end):
            if p_start > p_end: return None
            root = TreeNode(preorder[p_start])
            idx = hashMap.get(preorder[p_start])
            left_length = idx - i_start
            root.left = buildTree_helper(preorder, p_start+1, p_start+left_length, \
                                  inorder, i_start, idx - 1)
            root.right = buildTree_helper(preorder, p_start+left_length+1, p_end, \
                                   inorder, idx + 1, i_end)
            return root
        hashMap = {}
        for i, num in enumerate(inorder):
            hashMap[num] = i
        n = len(preorder)
        return buildTree_helper(preorder, 0, n-1, inorder, 0, n-1)





# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s.buildTree(preorder, inorder)