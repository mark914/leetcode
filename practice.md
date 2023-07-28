## 链表

160.Intersection of Two Linked Lists

```java
public ListNode getInteractionNode(ListNode headA, ListNode headB) {
    ListNode l1 = headA, l2 = headB;
    while(l1 != l2) {
        l1 = (l1 == null) ? headB: l1.next;
        l2 = (l2 == null) ? headA: l2.next;
    }
    return l1;
}


public ListNode getInteractionNode(ListNode headA, ListNode headB) {
    ListNode pA = headA, pB = headB;
    Set<ListNode> set = new HashSet<>();
    while(pA != null) {
        set.add(pA);
        pA = pA.next;
    }
    
    while(pB != null) {
        if (set.contains(pB)) {
            return pB;
        }
        pB = pB.next;
    }
    return null;
}

```



```python
def getInteractionNode(self, headA: ListNode, headB:ListNode) -> ListNode:
    pA, pB = headA, headB
    while A != B:
        A = A.next if A else headB
        B = B.next if B else headA
    
    return A

```

206.Reverse Linked List

```java
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) {
        return head;
    }
    
    ListNode reversed = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return reversed;
}
public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) {
        return head;
    }
    
    ListNode reversed = reverseList(head.next);
    head.next.next = head;
    head.next = null;
    return reversed;
}


public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) {
        return head;
    }
    
    ListNode p = head.next;
    head.next = null;
    ListNode temp;
    
    while (p != null) {
        temp = p;
        p = p.next;
        temp.next = head;
        head = temp;
    }
    return head;
}


public ListNode reverseList(ListNode head) {
    if (head == null || head.next == null) {
        return head;
    }
    ListNode p = head.next;
    head.next = null;
    ListNode temp;
    
    while (p != null) {
        temp = p;
        p = p.next;
        temp.next = head;
        head = temp;
    }
    
    return head;
}
```



```python
def reverseList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    p = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    
    return p


def reverseList(self, head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head
    p = head.next
    head.next = None
    
    while !p:
        temp = p
        p = p.next
        temp.next = head
        head = temp
        
    return head
```





21. Merge Two Sorted List

    ```java
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1 == null) return l2;
        if (l2 == null) return l1;
        
        if	(l1.val < l2.val) {
            l1.next = mergeTwoLists(l1.next, l2);
            return l1;
        } else {
            l2.next = mergeTwoLists(l1, l2.next);
            return l2;
        }
    }
    
    
    
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode p = dummy;
        while (l1 != null & l2 != null) {
            if (l1.val < l2.val) {
                p.next = new ListNode(l1.val);
                l1 = l1.next;
            } else {
                p.next = new ListNode(l2.val);
                l2 = l2.next;
            }
            p = p.next;
        }
        
        p.next = (l1 == null) ? l2:l1;
        
        return dummy.next;
    }
    ```

    ```python
    class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNoe) -> ListNode:
            if l1 is None:
                return l2;
            elif l2 is None:
                return l1;
            elif l1.val < l2.val:
                l1.next = self.mergeTwoLists(l1.next, l2)
            	return l1
            else:
                l2.next = self.mergeTwoLists(l1, l2.next)
                return l2
            
    class Solution:
        def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode(0)
            p = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    p.next = ListNode(l1.val)
                    l1 = l1.next
                    p = p.next
                else:
                    p.next = ListNode(l2.val)
                    l2 = l2.next
                    p = p.next
                
            p.next = l1 if l1 is not None else l2
            return dummy.next
    ```



83. Remove Duplicates from Sorted List

    ```java
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) return head;
        head.next = deleteDuplicates(head.next);
        return head.val == head.next.val ? head.next : head;
    }
    
    
    public ListNode deleteDuplicates(ListNode head) {
    	if (head == null || head.next == null) return head;
        ListNode cur = head;
        while (cur.next != null) {
            if (cur.val == cur.next.val) {
                cur.next = cur.next.next;
            } else {
                cur = cur.next;
            }
        }
        return head;
    }
    ```

    ```python
    class Solution:
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head
            head.next = self.deleteDuplicates(head.next);
            return head.next if head.val == head.next.val else head
        
    class Solution:
        def deleteDuplicates(self, head: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head
            cur = head
            while cur.next:
                if cur.val == cur.next.val:
                    cur.next = cur.next.next
                else:
                    cur = cur.next
    		return head
    ```



19.  Remove Nth Node from End of List

    -快慢指针

    -指针

    -stack

```java
public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode fast = head, slow = head;
    while (n-- > 0) {
        fast = fast.next;       
}
    if (fast == null) return head.next;
    while (fast.next != null) {
        fast = fast.next;
        slow = slow.next;
    }
    slow.next = slow.next.next;
    return head;
}


public ListNode removeNthFromEnd(ListNode head, int n) {
    private int getLength(ListNode head) {
        int length = 0;
        while (head != null) {
            head = head.next;
            length++;
        }
        return length;
    }
    
    length = getLength(head);
    ListNode dummy = new ListNode(0, head);
    cur = dummy;
    for (int i = 1; i < length-n; i++) {
        cur = cur.next;
    }
    cur.next = cur.next.next;
    return dummy.next;
}

public ListNode removeNthFromEnd(ListNode head, int n) {
    ListNode dummy = new ListNode(0, head);
    ListNode cur = dummy;
    Stack<ListNode> stack = new Stack<>();
    
    while (cur != null) {
        stack.push(cur);
        cur = cur.next;
    }
    
    while (n-- > 0) {
        stack.pop();
    }
    
    ListNode pred = stack.peek();
    pred.next = pred.next.next;
    return dummy.next;
}



```



```python
class Solution:
    def remoteNthFromEnd(head: ListNode, n: int) -> ListNode:
       	def getLength(head: ListNode) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
			return length
       dummy = ListNode(0, head)
       length = getLength(dummy)
       p = dummy
    	for i in range(1, length - n):
            p = p.next
		p.next = p.next.next
            
		return dummy.next

#stack
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        cur = dummy
        stack = list()
        while cur:
            stack.append(cur)
            cur = cur.next

        for i in range(n):
            stack.pop()
        
        pred = stack[-1]
        pred.next = pred.next.next
        return dummy.next

# fast slow cursor
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
"""
    purpose: 得到要删除前面的一位，倒数第n个和最后一个差几个，差n个，因此可以让fast 先走n个，然后一起走，保持差距。
    1.
    2.
    """
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if fast is None: 
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
                
                
```

24.swapPairs

```java
#length
public ListNode swapPairs(ListNode head) {
    ListNode dummy = new ListNode(0, head);
    ListNode p = dummy;
        
    while (p.next != null && p.next.next != null) {
        ListNode pred = p;
		ListNode left = p.next, right = p.next.next;
        
        pred.next = right;
        left.next = right.next;
        right.next = left;
      	p = p.next.next;
    }
    
    return dummy.next;
}


```

23. Swap Nodes in Pairs

    ```java
    //recursion
    public ListNode swapPairs(ListNode head) {
        // 1. special case head
        // 2. newHead, newHead.next, head
        if (head == null || head.next == null) {
            return head;
        }
    	ListNode newHead = head.next;
    	head.next = swapPairs(newHead.next);
        newHead.next = head;
        
        return newHead;
            
    }
    
    //iteration
    public ListNode swapPairs(ListNode head) {
        ListNode newHead = new ListNode(0, head);
        ListNode p = newHead;
        while (p.next != null && p.next.next != null) {
            temp = p;
            left = p.next;
            right = p.next.next;
           	//从temp->left->right 从前往后进行 
            temp.next = right;
            left.next = right.next;
            right.next = left;
            
            p = p.next.next;
        }
        
        return newHead.next;
    }
    
    ```

    ```python
    #iteration
    循环：要有起始条件，停止条件，同时也要向着停止条件进发
    class Solution:
        def swapPairs(self, head: ListNode) -> ListNode:
            dummy = ListNode(0, head)
            cur = dummy
    
            while cur.next and cur.next.next:
                temp = cur
                left = cur.next
                right = left.next
    
                temp.next = right
                left.next = right.next
                right.next = left
    
                cur = cur.next.next
            return dummy.next
    
    ##recursion
    class Solution:
        def swapPairs(self, head: ListNode) -> ListNode:
            if head is None or head.next is None:
                return head
            
            newHead = head.next
            head.next = self.swapPairs(newHead.next)
            newHead.next = head
    
            return newHead
    
        
    ```



445. Add Two Numbers

     ```java
     public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
         Stack<Integer> l1Stack = bulidStack(l1);
         Stack<Integer> l2Stack = bulidStack(l2);
         
         ListNode head = new ListNode(-1);
         int carry = 0;
         while (!l1Stack.isEmpty() && !l2Stack.isEmpty && carry != 0) {
             int x = l1Stack.isEmpty ? 0 : l1Stack.pop();
             int y = l2Stack.isEmpty ? 0 : l2Stack.pop();
             
             int sum = x + y + carry;
             ListNode node = new ListNode(sum%10);
             carry = sum/10;
             node.next = head.next;
             head.next = node;
             
         }
         return head.next;
         
     }
     
     ```

     

```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def buildStack(l1: ListNode)->list:
            stack = []
            while l1:
                stack.append(l1.val)
                l1 = l1.next
            return stack

        l1Stack = buildStack(l1)
        l2Stack = buildStack(l2)

        head = ListNode(0)
        carry = 0
        while l1Stack or l2Stack or carry != 0:
            x = l1Stack.pop() if l1Stack else 0
            y = l2Stack.pop() if l2Stack else 0
            sum = x + y + carry

            node = ListNode(sum%10)
            carry = sum//10
            
            node.next = head.next
            head.next = node
            

        return head.next
    

```



234. Palindrome Linked List

     ```java
     // 链表后向遍历
     1. 链表后向遍历
     2. left 和 right 一一比较
     public ListNode left;
     public boolean isPalindrome(ListNode head) {
         left = head;
         return traverse(head);
     }
     public boolean traverse(ListNode right) {
         
     }
     
     
     // 快慢指针方法
     1. 用快慢指针，找到链表中间靠后位置
     2. 将后面的翻转
     3. 比较是否相等。
         看labuladong的题解
     public boolean isPalindrome(ListNode head) {
             ListNode fast = head;
             ListNode slow = head;
             while (fast != null && fast.next != null) {
                 fast = fast.next.next;
                 slow = slow.next;
             }
     
             if (fast != null) slow = slow.next;
             
             ListNode left = head;
             ListNode right = reverse(slow);
     
             while (right != null) {
                 if (left.val != right.val) {
                     return false;
                 }
                 left = left.next;
                 right = right.next;
             }
             return true;
         }
     
     
         public ListNode reverse(ListNode head) {
             if (head == null || head.next == null) {
                 return head;
             }
             ListNode p = head.next;
             head.next = null;
             ListNode temp;
     
             while (p != null) {
                 temp = p;
                 p = p.next;
                 temp.next = head;
                 head = temp;
             }
     
     
             return head;
     
         }
     ```

     

     ```python
     #LinkNode 2 List
     class Solution:
         def isPalindrome(self, head: ListNode) -> bool:
             vals = []
             cur = head
             while cur:
                 vals.append(cur.val)
                 cur = cur.next
                 
            	return vals == vals[::-1]
     
     
     ## 递归的方法， 也就是对链表进行后向遍历（回溯算法）
     class Solution:
         
         def isPalindrome(self, head: ListNode) -> bool:
             self.left = head
             return self.traverse(head)
         
         def traverse(self, right: ListNode) -> bool:
             if right is None:
                 return True
             res = self.traverse(right.next)
             res = res and (self.left.val == right.val)
             self.left = self.left.next
     
             return res
              
     
     
     ```

     

725. Split Linked list in parts

     ```java
     public ListNode[] splitListToParts(ListNode root, int k) {
         int length = getLength(root);
         int size = length / k;
         int mod = length % k;
         
         ListNode[] ret = new ListNode[k];
         ListNode cur = root;
         for (int i = 0; i < k && cur != null; i++) {
             ret[i] = cur;
             int curSize = (mod > 0) ? (size + 1) : size;
             mod = mod - 1;
             
             while (cur-- > 1) {
                 cur = cur.next;
             }
             ListNode next = cur.next;
             cur.next = null;
             cur = next;
         }
     }
     
     ```

     

```python
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        def getLength(head: ListNode) -> int:
            n = 0
            while head:
                head = head.next
                n += 1
            return n
        length = getLength(head)

        size, mod = length // k, length % k

        ret = [None for _ in range(k)]
        cur = head
        i = 0

        while i < k and cur:
            ret[i] = cur
            curSize = size + (1 if i < mod else 0)
            
            for _ in range(curSize-1):
                cur = cur.next

            temp = cur.next
            cur.next = None
            cur = temp
            i += 1

        return ret
```



328. 奇偶链表

     ```python
     class Solution:
         def oddEvenList(self, head: ListNode) -> ListNode:
             # 创建两个链表
             # 判断奇偶，得到奇偶列表
             # 偶列表连在奇列表后
             if not head:
                 return head
             
             evenList = head.next
             odd, even = head, evenList
     
             while even and even.next:
                 odd.next = even.next
                 odd = odd.next
                 even.next = odd.next
                 even = even.next
     
             odd.next = evenList
             return head
     ```

     

剑指06.从尾到头打印链表

```java
class Solution{
    public List<Integer> ret = new ArrayList<>();
    public int[] reversePrint(ListNode head) {
        List<Integer> temp = recur(head);
        int size = temp.size();
        int[] ret = new int[size];
        
        for (int i = 0; i < size; i++) {
            ret[i] = temp.get(i);
        }
        return ret;
    }
    
    public List<Integer> recur(ListNode head) {
        if (head == null) return ret;
        ret = recur(head.next);
        ret.add(head.val);
        return ret;
    }
}
```





```python
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        
```







## 树

104. Maximum Depth of Binary Tree

```java
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        
        int left = maxDepth(root.left);
        int right = mexDepth(root.right);
        
        return Math.max(left, right) + 1;
    }
}



res = 0;
depth = 0;
public int maxDepth(TreeNode root) {
    traverse(root);
    return res;
}
public void traverse(TreeNode root) {
    if (root == null) {
        return;
    }
    res = Math.max(res, depth);
    depth++;
    traverse(root.left);
    traverse(root.right);
    depth--;
}
```

```python
class Solution:
    def maxDept(root: TreeNode) -> int:
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        return max(left, right) + 1
```





110. Balanced Binary Tree

```python
class Solution:
    result = True
    def isBalanced(self, root: TreeNode) -> bool:
        self.maxDepth(root)
        return reslut
    def maxDepth(self, root):
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if abs(left - right) > 1:
            result = False
		
        return max(right, left) + 1
    
    
class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:
        self.result = True
        def maxDepth(self, root):
            if root is None:
                return 0
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            if abs(left - right) > 1:
                self.result = False
		
            return max(right, left) + 1 
        maxDepth(root)
        return self.reslut
       

        
```





543. Diameter of Binary of Tree

     ```python
     class Solution:
         def diameterOfBinaryTree(root):
             self.ans = 0
             
             def maxDepth(root):
                 if root is None:
                     return 0
                 left = maxDepth(root.left)
                 right = maxDepth(root.right)
                 self.ans = max(self.ans, left+right)
                 return max(left, right) + 1
             
             maxDepth(root)
             return self.ans
     
     ```

     

226. Invert Binary Tree

     ```python
     class Solution:
         def invertTree(self, root):
             if root is None:
                 return None
             left = root.left
             root.left = root.right
             root.right = left
             return root
     ```

     

617. Merge Two Binary Tree

     ```python
     class Solution:
         def mergeTrees(self, t1, t2):
             """
             :type t1: TreeNode
             :type t2: TreeNode
             :rtype: TreeNOde
             """
             if not t1: return t2
             if not t2: return t1
             root = TreeNode(t1.val + t2.val)
             root.left = self.mergeTrees(t1.left, t2.left)
             root.right = self.mergeTrees(t1.right, t2.right)
             
             return root
     ```

     

112. Path sum

     ```python
     class Solution:
     	def hasPathSum(self, root, sum):
             """
             :type root: TreeNode
             :type sum: int
             :rtype: bool
             """
          	if not root:
             	return False
             if root.left is None and root.left is None and root.val == sum:
                 return True
             return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-rootval)
         
             
     ```

     

437. Path SumII

     ```python
     class Solution:
         def pathSum(self, root, sum):
             """
             :type root: TreeNode
             :type sum: int
             :rtype: int
             """
             def includeRoot(root, sum):
                 num = 0
                 if root is None:
                     return 0
                 if root.val == sum:
                     num += 1
     			l = includeRoot(root.left, sum-root.val)
                 r = includeRoot(root.right, sum-root.val)
                 num += l+r
                 
                 return num
             
             if root is None:
                 return 0
             self.ret = includeRoot(root, sum) + pathSum(root.left, sum) + pathSum(root.left, sum)
             
             
             return self.ret
             
     ```

     

527. Subtree of Another Tree

     ```python
     class Solution:
         def isSubtree(self, s, t):
             """
             :type s: TreeNode
             :type t: TreeNode
             :rtype: bool
             """
             def isSubtreeWithRoot(s, t):
                 if not s and not t:
                     return True
                 if not s or not t:
                     return False
                 if s.val != t.val:
                     return False
                 return isSubtreeWihtRoot(s.left, t.left) and isSubtreeWithRoot(s.right, t.right)
             
             if not s:
                 return False
             return isSubtreeWithRoot(s, t) or isSubtree(s.left, t) or isSubtree(s.right, t)
         
     
     ```

     

111. Minimum Depth of Binary Tree

     ```python
     class Solution:
         def minDepth(self, root: TreeNode) -> int:
             if not root:
                 return 0
             depth = 1
             queue = [root]
     
             while len(queue) > 0:
                 for _ in range(len(queue)):
                     node = queue.pop(0)
                     if not node.left and not node.right:
                         return depth
                     if node.left:
                         queue.append(node.left)
                     if node.right:
                         queue.append(node.right)
     
                 depth += 1
             
             return depth
         
         
         
         
      
     def minDepth(root):
         if not root:
             return 0
         queue = [root]
         depth = 1
         
         while queue:
             for _ in range(len(queue)):
                 node = queue.pop(0)
                 if not node.left and not node.right:
                     return depth
                 if node.left:
                     queue.append(node.left)
     			if node.right:
                     queue.append(node.right)
                     
     		depth += 1
         
     	return depth
     ```

     

## 二分查找

69.Sqrt(x)

```python
class Solution:
    def mySqrt(self, x):
        l, r = 1, x
        while l <= r:
            mid = l + (r-1)/2
            sqrt = x/mid
            if mid == sqrt:
                return mid
            elif mid < sqrt:
                l = mid + 1
			elif mid > sqrt:
                r = mid -1
		return r
            
        
```

774. Find Smallest Letter Greater Than Target(Easy)

     ```python
     def nextGreatestLetter(letters, target):
         l = 0
         r = len(letters) - 1
         while l <= r:
             m = l + (r - l)/2
             if letters[m] <= target:
                 l = m+1
     		elif letters[m] > target:
                 h = m-1
     ```

     
