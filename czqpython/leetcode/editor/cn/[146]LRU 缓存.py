# 请你设计并实现一个满足 LRU (最近最少使用) 缓存 约束的数据结构。 
# 
#  实现 LRUCache 类： 
# 
#  
#  
#  
#  LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存 
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
#  void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 
# key-value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。 
#  
# 
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 
#  
#  
# 
#  
# 
#  示例： 
# 
#  
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= capacity <= 3000 
#  0 <= key <= 10000 
#  0 <= value <= 10⁵ 
#  最多调用 2 * 10⁵ 次 get 和 put 
#  
#  Related Topics 设计 哈希表 链表 双向链表 👍 1937 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class LRUCache(object):

    class LRUCache:

        def __init__(self, capacity: int):
            self.capacity = capacity
            self.cache = DoubleList()
            self.map = dict()

        def get(self, key: int) -> int:
            if key not in self.map:
                return -1
            x = self.map[key]
            # make most recently
            self.makeRecently(key)
            return x.val

        def put(self, key: int, value: int) -> None:
            if key in self.map:
                x = self.map[key]
                # delete x and put x recently
                self.delete(key)
                # add key val
                self.addRecent(key, value)
                return

            if self.capacity == len(self.map):
                self.deleteLeastRecently()
            self.addRecent(key, value)

        def makeRecently(self, key):
            x = self.map[key]
            self.cache.remove(x)
            self.cache.addLast(x)

        def delete(self, key):
            x = self.map[key]
            self.cache.remove(x)
            self.map.pop(key)

        def addRecent(self, key, val):
            x = Node(key, val)
            self.cache.addLast(x)
            self.map[key] = x

        def deleteLeastRecently(self):
            # delete first
            first = self.cache.removeFirst()
            key = first.key
            self.map.pop(key)

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
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
        self.pre.next = x
        self.tail.pre = x
        self.size += 1

    def remove(self, x):
        x.pre.next = x.next
        x.next.pre = x.pre
        self.size -= 1

    def removeFirst(self):
        if self.head.next == self.tail:
            return None
        first = self.head.next
        self.remove(first)
        return first

    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()