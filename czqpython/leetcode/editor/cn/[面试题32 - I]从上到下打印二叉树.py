# 从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。 
# 
#  
# 
#  例如: 
# 给定二叉树: [3,9,20,null,null,15,7], 
# 
#      3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回： 
# 
#  [3,9,20,15,7]
#  
# 
#  
# 
#  提示： 
# 
#  
#  节点总数 <= 1000 
#  
#  Related Topics 树 广度优先搜索 二叉树 👍 157 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                res.append(node.val)
                if not node.left:
                    queue.append(node.left)
                if not node.right:
                    queue.append(node.right)
        return res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()
    s.levelOrder([3,9,20,null,null,15,7])
