### 	连等

```python
a = b = 1
# a = 1, b = 1
```



### 栈

```python
# stack，使用list来代替栈
stack = list()
stack.append()
stack.pop()
stack[-1]

```

### queue

```python
# queue, 用list来代替
queue = list()
queue.append()
queue.pop(0)

```



### List

```python
arr
## create 
list()
list(range(10))
[]
[expr for val in collection if condition]

## slice
arr[5]
arr[3:5]
arr[:5]
arr[:-1]
arr[:]
arr[2:4] = 100
arr[1:-1:2]
arr[::-1]
arr[-10:]

## method
arr.index("src")

arr.append("src")
arr.extend([1, 2, 3])
arr.insert(2, "src")

arr.pop()
arr.remove("src")
arr.count(obj)

arr.reverse() # return None
reversed(arr) # return reversed array
arr.sort()

## other methods
enumerate(a)
for i, value in enumerate(collection):

map(func, iteratable)
filter(func, iterable)

zip(first_iter, second_iter)
reversed(sequence)

## 判断列表是否为空
while l:
    
    
## list初始化
c=[i for i in range(10) if i%2==0 and i<8]
a = [-1 for _ in range(10)]


## 向list中添加元素,用索引或者append
res = []
for num in nums:
    nextGreater = map.get(num, -1)
    res.append(nextGreater)

res = [-1 for _ in range(len(nums1))]
for i in range(len(nums1)):
    res[i] = map.get(nums1[i], -1)
    
    
ret = [None for _ in range(k)]

# 在函数中对list进行修改
a[:] = b
而不应该是
a = b


# 循环数组，列表循环，改变起始点，
##使用注意其实位置+数量+j % n
##从第i+1到第i-1
for j in range(i+1, n+i):
    print(j % n)
    i+1
    i+2
    n-1
    0
    1
    2
    …
    i-1
如果是减去1
(j - 1 + length) % length
0 - 9  lenght = 10
9 - 1 + 10 % 10 = 8
0 - 1 + 10 % 10 = 9
如果是加上1
(j + 1) % length
0 - 9 length = 10
9 + 1 % 10 = 0
    
## 可以让后进的放在最前面， 之字形打印
reverse = False
reverse = not reverse
```

### math

```python
## 整除
a //b
## 除法
a / b
## 取模
a % b
```



### 判断是否为空

```python
if fast:

and
or

```



### nolocal

```python
cs61a里面有
弄够对parent 环境中的变量进行修改。
```



### python类中的多函数

尽量使用嵌套函数

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



### python换行

```python
反斜杠\ 换行
```



### int

```python
int()将数据转化为整数类型
```



### str 与list的相互转换

```python
##list2str
list1 = ['life', 'is','easy']
str1 = " ".join(list1)

##str2list
str2 = life
list2 = list(str2)

## str 的切片可以达到修改str的目的
p = "123"
p += "2"
p = p[:-1]
## 利用list和str之间的相互变换，也能够达到修改str的目的, 使用这个要求s中的每一个元素都是字符才可以
list1 = "".join(s)

## 但是应该注意s为空字符串的特殊情况
"".join([]) = ""
## s[i]的结果也为str

```





### 循环

```python
## python不支持动态修改for循环中变量
def canJump(nums):
    ## 这里每次循环都会对cover进行改变，然而这是不允许的，因此不可以
    cover = 0
    for i in range(cover + 1):
        cover = max(cover, i + nums[i])
        if cover >= len(nums) - : return True
    return False

## 使用while代替
def canJumpy(nums):
    cover = 0
    i = 0
    while i <= cover:
        cover = max(cover, i + nums[i])
        if cover >= len(nums) - 1: return True
    return False
# 使用index
## 用for
for i in range(len(nums)):
## 从i+1循环到i-1， 使用range(i , j)来定义循环，这个非常重要。
for i in range(i+1, n+i):
    print(i % n)
    
    
## 用while
i = 0
while i < len(nums):
    i += 1

# 使用value

for num in nums:
    
    

```



### deque

```python
append(x)
appendleft(x)
clear()
copy()
count()
extendleft()
pop()
popleft()
a = deque([1, 2, 3])
a[-1]
```



### bool

```python
empty：
return not stack1 and not stack2

not empty：
if stack：

## and表示一个条件，取交集
## or 表示多个条件，取并集

```



### 整数的最大值和最小值

```python
import sys
max = sys.maxsize
min = -sys.maxsize -1
## 最大和最小
float("inf")
float("-inf")
```



### 求一列数的出现次数最多的值（有多个）

```python
res = []
map
maxTimes = -sys.maxsize - 1
for num, times in map.items():
    if times == maxTimes:
        res.append(num)
    elif times > maxTimes:
        maxTimes = times
        res.clear()
        res.append(num)
```



### heap

```python
## 小顶堆可以用来保存最大的k个数，因为小顶能够很方便的得到现有的最小元素，从通过不断排除最小元素，得到最大的k个数
## 大顶堆可以用来保存最小的k个数，因为大顶能够很方便的得到现有的最大元素，从而通过不断排除最大元素，得到最小的k个数

heapq.heapify(list)
heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heappushpop(heap, item)
## heapreplace(nums, nums[0] + 1)
heapq.heapreplace(heap, item) 
heapq.nlargest(n, iterable, key=None)  == sorted(iterable)[:n]


heap实现从小到大排序：
heap = []
for key in map:
    heapq.heappush(heap, (map[key], key))

heap 实现从大到小排序：
heap = []
for key in map:
    heapq.heappush(heap, (-map[key], key)

# 源码： https://segmentfault.com/a/1190000017793857
# 使用heap时注意，heap是使用list实现的，因此可以用[]直接创建，并且其实就是list表示的，因此可以用用list的方法操作（但这样会改变heap的结构），也可以用heap的方法进行操作。
heap中heap[0]就是最小/最大的元素
```



### map

```python
# map排序
## 按val排序
res = sorted(map.items(), key = lambda kv: kv[1])

## 按key排序
res = sorted(map.items(), key = lambda kv: kv[0])

sum(map(int, str(num)))

## 字典获取元素
# 获取元素尽量使用.get, 尽量使用dict.get
nextGreater = map.get(num, -1)

## 初始化，不要使用
dit1 = dit2 = {}
## 因为这个是引用，不是创建一个新的字典
```



### 交换

```python
a, b = b, a
先计算后面，然后将值赋给a，再赋给b
等价于：
c = a
a = b
b = a
同时要注意一些对赋值顺序敏感的交换
nums[i] 和nums[nums[i]]之间的交换。如果先对nums[i]进行赋值，就会导致nums[nums[i]]中的nums[i]发生变化，从而出现问题。所以应该先对nums[nums[i]]进行赋值。
nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
```



### 求一组数的最大值

```python
maxVal = -sys.maxsize - 1
for num in nums:
    maxVal = max(maxVal, num)

# 返回最大的数 
return max(dp(i) for i in range(len(nums)))
```



### Counter

```python
c =Counter(nums)
c = dict(c) #转换为dictory，从而可以进行迭代操作。
c.items()
c.keys()
c.values()
sorted(c.items(), reverse = True)
## Return a list of the n most common elements and their counts from the most common to the least. If n is not specified, most_common() returns all elements in the counter. Elements with equal counts are ordered arbitrarily
c.most_common(1) # 得到最常出现的值及其出现的次数
c.most_common()

```



### range 和 xrange

```python
在python3中xrange被简写为range，得到的是一个生成器
range(0, 3, 2)
#倒序，这个一定要加-1，否则是不行的
range(3, 1, -1)
range(start, stop, step)

```

## 二分法中找到合适的位置

```
也就是找到大于等于它的第一个元素	
```





### 统计区间长度

```python
## 半开半闭区间，[i, j）： 直接两个相减 j - i
## 故意使用左闭右开
while i < n-1 and ratings[i] < rating[i+1]:
    i += 1
## 闭区间[i,j]： 相减之后加1 j - i + 1
## 要长度为k的区间
[i, i+k)
 ## 每隔长度k设置一个区间
 首先确定起点，然后起点+长度确定区间
 i += k
 [i, i+k)
 [i+k, i+2k)
 [i+2k,i+3k)
 类似于这种
  
  用区间的知识去理解：

[i, j] 为例： 区间长度为j - i + 1

[i, j），其中i未知，满足条件的区间length已知， i坐标为i = j - length.
```



### syntax

```python
''.join(a.sort())是错误的，因为a.sort()是没有返回值的（修改）
''.join(sorted(a))是对的，因为sorted(a)是有返回值的（产生一个新的）

```





### 错误

debug相关，如何进行debug，很重要，要多看看。

多使用assert确定得到的结果是你想要的



### 判断

函数`str.isdigit()`判断字符是否为数字，函数`str.isalpha()`判断字符是否为字母，函数`isalnum()`判断字符是否为数字字母组合。	



### 除法

```python
## / 为除法 //为向下取余（负无穷取余） int(-12/10)为取整
print(-12/10)
print(int(-12/10))
print(-13//10)
```

### 找到第一个不相等的位置：

找到第一个不相等的点：

关键，

```python
## 方法一
left = nums[i] 
while l < r and nums[l] == left: l += 1
    
## 方法二 使用nums[l]时，一定要注意取值。
while l < r and nums[l] == nums[l+1]: l += 1
l += 1
```



这里非常有意思。

### 矩阵遍历

```python
# 使用两个变量
for i in range(m):
    for j in range(n):
        print(grid[i][j])
# 使用一个变量
idx = 0
while idx < m*n:
    print(grid[idx/n][idx%n])
```



### 字符串

```python
# 没有参数很厉害，None (the default value) means split according to any whitespace,and discard empty strings from the result.返回结果为字符列表
strs.split()
## 每隔一段进行处理
text = input().strip()
length = len(text)
i = 0
while i < length:
    if i + 8 <= length:
        print(text[i:i+8])
    else:
        print(text[i:]+'0'*(8-(length-i)))
    i += 8

## # Use str type's split() method
# https://www.cnblogs.com/klchang/p/13974651.html
print("aa\\bb".split("\\"))
## 替换
s.replace(' ', '%20')
```



### kmp问题

暴力算法

```python
n, m = len(text), len(pattern)
## 这里是因为要匹配，必须使得后面的长度大于等于m，最小为m，则为n-m位置
for i in range(n-m+1):
    j = 0
    ## 这里不能使用for循环，因为for循环无法判断最后一个是否匹配。
    ## 如果匹配返回m-1，不匹配返回的也是m-1。for循环j最后的大小会固定，要用while循环，最后停的位置为m时，则成立。
    while j < m:
        if pattern[j] != text[i+j]:
            break
        j += 1
    if j == m: return i
return -1
        
```

如果要用循环变量i来进行判断的话，一定要使用while循环。因为for循环中的i最后的大小是固定的，并且不能再外面使用

kmp算法

```python
## buildMatch
def buildMatch(pattern):
    pass
def KMP(text, pattern):
    
    

```



防止超时：

应该每次乘完以后再取模，确保乘法的每个操作数不会太大！否则就会出现超大整数相乘，从而导致超时。

```python
MOD = 10 ** 9 + 7
for num in nums:
            ans = ans * num % MOD
return ans

```



### map，filter

```python
def getSum(strs: str) -> int:
            res = sum(map(int, strs))
            return res
```



### ascii

```python
ord()函数主要用来返回对应字符的ascii码，chr()主要用来表示ascii码对应的字符他的输入时数字，可以用十进制，也可以用十六进制。
ord
chr
c.lower()
c.upper()
```



### 测试

```python
print 和 assert
test = ['01', '0', '', '00']
    test_res = [False, True, False, False]
    for t, t_r in zip(test, test_res):
        assert isValid(t) == t_r,  f'{t}'	 


```

对类的测试

```python
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
>>>x = 7
>>> eval( '3 * x' )
21
getattr(obj, f)(*p) 得到obj的f对象，然后给它参数
def print_result(funs, paras):
    res = []
    obj = None
    for i, (f, p) in enumerate(zip(funs, paras)):
        if i == 0:
            res.append(obj)
            obj = eval(f)(*p)
        else:
            res.append(getattr(obj, f)(*p))
    print(res)
f = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
s = [[], [-2], [0], [-3], [], [], [], []]
print_result(f, s)

def print_result(funs, paras):
    res = [None]
    obj = eval(funs[0])(*paras[0])
    for f, p in zip(funs[1:], paras[1:]):
        res.append(getattr(obj, f)(*p))
    print(res)


```

### 测试用例

```python
##长度为1或为0的数组
arr = []
arr = [0]
```



### 返回两个数拼接起来的最大值

```python
def merge(A: List[int], B: List[int]) -> List[int]:
    ans = []
    while A or B:
        bigger = A if A > B else B
        ans.append(bigger.pop(0)) 
	return ans
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
```

### 求删除k个数之后的最大值

```python
# 用stack来进行处理，保持有序，单调栈。
def pickMax(nums, k):
    stack = deque()
    drop = len(nums) - k
    for num in nums:
        while stack and drop and stack[-1] < num:
            stack.pop()
            drop -= 1
    stack.append(num)
    return list(stack)[:k]
```



#### 排序数组（bisect）



```python
## SortedList的使用
##from sortedcontainers import SortedList
from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        sl = SortedList()
        nums = nums[::-1]
        for i in range(n):
            cnt = sl.bisect_left(nums[i])
            res[i] = cnt
            sl.add(nums[i])
        
        return res[::-1]
 Python中bisect的用法及示例详解 https://cloud.tencent.com/developer/article/1733600
import bisect
bisect 函数其实是 bisect_right 函数的别名
bisect_left 返回的插入位置是原序列中跟被插入元素相等的元素的位置， 也就是新元素会被放置于它相等的元素的前面， 而 bisect_right 返回的则是跟它相等的元素之后的位置。 
(如何不存在的话就会返回合适的位置)
主要针对有序元素
bisect.insort
用bisect.insort插入新元素

你可以先用 bisect(haystack, needle) 查找位置 index， 再
用 haystack.insert(index, needle) 来插入新值。

insert某个位置，则是插入到该位置原来元素的前面。
bisect是找到相等元素后面的位置
bisect_left是找到相等元素前面的位置
如果是要找到x所在的位置，还是要使用bisect_left来查找
import bisect
idx = bisect.bisect_left(nums, x)

```



### random

```python
生成均匀分布
random.uniform(self.x-self.r, self.x+self.r)
对nums进行随机重排
random.shuffle(nums)
random.randint(low, high) 不包括high
```



### 进制转换



### 比较函数

```python
def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        temp = list(map(str,nums))
        temp.sort(key = cmp_to_key(lambda x,y:int(x+y)-int(y+x)),reverse = True )
        return ''.join(temp if temp[0]!='0' else '0')

```





### 快速幂和快速乘法

用来计算a**b和a与b的乘积

方法：

首先将b看做是二进制，然后将二进制转化为十进制，二进制的每一位只能为1或者0，如果是1，那么它表示的就是2**i。

如果是快速幂$a**b = a**(b_{n-1}*2^{n-1} + ... + b_1*1)$

这样就可以使用迭代： $a, a^2, a^4, ..., a^{2^{n-1}}$, ……， 

递推公式就可以写成：a = a*a

如果是快速乘法 $a*b = a*(b_{n-1}2^{n-1} + b_1*2^0)$

$a, a*2, a*4, a*8, a*(2^{n-1})$

递推公式就可以写成 a += a

### 知识点总结：

排序，求最大最小数，链表，大数、高精度数运算，字符串常见操作，数组常见操作，四则运算，求数的各种附属数，匹配问题，进制转换，二叉树，规划问题，最短路径问题，图联通问题，对数字进行特殊判断。



递归、分治、单调栈、并查集、滑动窗口、前缀和、查分、[二分查找](https://www.nowcoder.com/jump/super-jump/word?word=二分查找)、BFS广搜、DFS深搜

回溯算法关键在于选择，在于对树的遍历

### 常见错误

字符串，矩阵长度为0时，需要特殊处理

层序遍历一般是queue需要从queue.popleft(), 层序遍历的本质思想就是一层一层遍历

找到题目中所有的变量，根据变量确定要求的状态 

三个变量[688. 骑士在棋盘上的概率](https://leetcode.cn/problems/knight-probability-in-chessboard/)

将数组为空作为一个条件

找到k个相当于删除n-k个

如果出现每个元素都不同，则需要考虑使用二分、hash等方法

要求满足要求的最大数，可以考虑二分、动态规划

将node放到queue里面说明会访问到他，如果没有放，则说明不会访问到。使用dfs的时候注意是否要把某个节点放到结果中去。bfs + dp的解法

