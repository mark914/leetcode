## build Tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
from collections import deque
## array and tree
def getTree(nums):
    res = []
    root = None
    for i in range(len(nums)):
        node = None
        if nums[i] != 0:
            node = TreeNode(nums[i])
        res.append(node)
        if i == 0:
            root = node
    i = 0
    while 2 * i + 2 < len(nums):
        if not res[i]: continue
        res[i].left = res[2 * i + 1]
        res[i].right = res[2 * i + 2]
        i += 1
    return root

## tree to array
def getNum1(root):
    if not root: return []
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur:
                res.append(cur.val)
                queue.append(cur.left)
                queue.append(cur.right)
            else:
                res.append(0)
    return res

## tree to array(null)
def getNum(root):
    if not root: return []
    queue = deque()
    queue.append(root)
    res = []
    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            res.append(cur.val)
            if cur.left: queue.append(cur.left)
            if cur.right: queue.append(cur.right)
    return res

## 链表
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

## 双向链表
class Node:
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.pre = None
        self.next = None
class DoubleList:
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0
    def addLast(self, x):
        x.pre = self.tail.pre
        x.next = self.tail
        self.tail.pre.next = x
        self.tail.pre = x
        self.size += 1
    def remove(self, x):
        x.pre.next = x.next
        x.next.pre = x.pre
        self.size -= 1
    def removeFirse(self):
        if self.head.next == self.tail:
            return None
        else:
            first = self.head.next
            self.remove(first)
            return first




if __name__ == "__main__":
    arr = [1, 1, 2, 0, 0, 4, 5]
    print(arr)
    tree1= getTree(arr)
    print(tree1)
    arr2 = getNum(tree1)
    print(arr2)
