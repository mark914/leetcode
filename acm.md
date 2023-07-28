输入包括两个正整数a,b(1 <= a, b <= 1000),输入数据包括多组。

- 这里并没有说要输入多少组测试数据，因此需要让while语句能够停下来，就使用try， except语句，如果出现不符合要求的数据，就停止。

```python
while True:
    try:
        nums = input().strip().split(' ')
        nums = list(map(int, nums))
        print(sum(nums))
    except:
        break
while True:
    try:
        nums = list(map(int, input().split()))
        print(nums)
    except:
        break

```



输入第一行包括一个数据组数t(1 <= t <= 100)
接下来每行包括两个正整数a,b(1 <= a, b <= 1000)

```python
if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        nums = input().strip().split()
        nums = list(map(int, nums))
        print(sum(nums))
```



输入包括两个正整数a,b(1 <= a, b <= 10^9),输入数据有多组, 如果输入为0 0则结束输入

```python
if __name__ == "__main__":

while True:
     nums = list(map(int, input().strip().split()))
     if nums == [0, 0]: break
     print(sum(nums))
```



输入数据包括多组。
每组数据一行,每行的第一个整数为整数的个数n(1 <= n <= 100), n为0的时候结束输入。
接下来n个正整数,即需要求和的每个正整数。

- 先读题，然后再去写
- 如果没有说明什么时候结束，就使用try， except

```python
while True:
    try:
        nums = list(map(int, input().split(' ')))
        if nums[0] == 0 : break
        print(sum(nums[1:]))
    except:
        break
        
while True:
    try:
        nums = list(map(int, input().split(" ")))
        if nums[0] == 0: break
            print(sum(nums[1:]))
		except:
            break
```



输入的第一行包括一个正整数t(1 <= t <= 100), 表示数据组数。
接下来t行, 每行一组数据。
每行的第一个整数为整数的个数n(1 <= n <= 100)。
接下来n个正整数, 即需要求和的每个正整数。

```python
t = int(input().strip())
for _ in range(t):
    nums = list(map(int, input().split(' ')))
    print(sum(nums[1:]))
```





输入数据有多组, 每行表示一组输入数据。
每行的第一个整数为整数的个数n(1 <= n <= 100)。
接下来n个正整数, 即需要求和的每个正整数。

```python
while True:
    try:
        nums = list(map(int, input().split(" ")))
        print(sum(nums[1:]))      
    except:
        break
```



输入有两行，第一行n

第二行是n个字符串，字符串之间用空格隔开

```python
t = int(input())
arr = input().split(" ")
arr.sort()
print(" ".join(arr))
```





字符串输出：

```python
count = int(input())
arr = list(map(int, input().strip().split()))
s = int(input())

if s:
    print(" ".join(map(str,sorted(arr)[::-1])))
else:
    print(" ".join(map(str, sorted(arr))))
```





输入输出：

```python
input()
float()
int()
set()

print()
def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
    """
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
    
## 用空格隔开
print(num, end=' ')

## 输出结果
for c in res:
    print(c)
```





## 华为机试

四舍五入

```
import math
# 向下取整
math.floor()
# 向上取整
math.ceil()
# 四舍五入（2.5 -》2）
round()
int(num + 0.5)
```

提取不重复整数：

```python
#1. 有顺序 2. 去重 -》 使用[]

num = input()
num = num[::-1]
res = []
s = set()
for elem in num:
    if elem in s: continue
    res.append(elem)
    s.add(elem)
res = ''.join(res)
print(res)
        
```



找出连续最长数字串

判断是否为数字

str为字符串s为字符串

str.isalnum() 所有字符都是数字或者字母

str.isalpha() 所有字符都是字母

str.isdigit() 所有字符都是数字

str.isspace() 所有字符都是空白字符、t、n、r



使用queue解题，不过要注意改变maxL的取值。



**HJ90** **合法IP**

要注意各种边界条件：

首先是如何分割ip，     ip = list(input().strip().split('.'))

然后怎么样才是合法的部分：

- 长度大于0 len(strs)
- 长度大于1时，首位不为0 
- 要为数字，且要在0到255之间 isdigit



**HJ26** **字符串排序**

关键实在



**HJ19** **简单错误记录**

```python
## split的使用
s = list(map(str, input().strip().split('\\')))
## list索引的使用
a = ss[0][-16:] + " " + ss[1]
## 使用两个list来替代有序map的使用
res = []
cnt = []

```



**HJ25** **数据分类处理**

关键：读题是非常关键的，只有读懂了题目，才知道是要你做什么。抓住要处理的变量。先看示例，再看输出的形式。



进制之间的转换

https://blog.csdn.net/weixin_42317507/article/details/90315848



**HJ41** **称砝码**

求所有的和的set，用set进行去重

```python
for i in range(n):
    tmp = [m[i] * j for j in range(x[i]+1)]
    res = list(set(a + b for a in tmp for b in res))
```

