# 输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。 
# 
#  示例1： 
# 
#  输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4 
# 
#  限制： 
# 
#  0 <= 链表长度 <= 1000 
# 
#  注意：本题与主站 21 题相同：https://leetcode-cn.com/problems/merge-two-sorted-lists/ 
#  Related Topics 递归 链表 👍 223 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            val1, val2 = l1.val, l2.val
            if val1 < val2:
                p.next = ListNode(val1)
                l1 = l1.next
            else:
                p.next = ListNode(val2)
                l2 = l2.next
            p = p.next
        p.next = l2 if not l1 else l1
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()