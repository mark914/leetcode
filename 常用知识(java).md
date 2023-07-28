## List

```java
//build
List<Integer> a = new ArrayList<>();
//get
a.get(i);
//add
a.add(int);

//List to array
//method one
List<Integer> x = new ArrayList<>();
int[] y = x.toArray();

//method two
//当有reference的时候就需要进行指定，使用这种方法。
List<int[]> res = new ArrayList<>();
int[][] ress = res.toArray(new int[res.size()][]);
```



## array

```java
# build
int[] a = new int[k];
int[] a = {1, 2, 3};
int[][] a = {{1, 2}, {2,1}}
int rows = a.length, col = a[0].length;

## instantiation and assignment
int[] a;
a = new int[]{1, 2, 3}
如果instantiation 和 assignment分开的话，就不能省略掉new int[]

# access
a[0];

# length
a.length;

# loop
for (int x: a) {
    System.out.println(x);
}

# multiDimensional arrays
int[][] myArray = new int[1][2];

Arrays.fill(dp, 1)
```



## Stack

```java
// 创建
 Stack<Integer> a = new Stack<Integer>();
// 是否为空
 boolean a.empty()
// 查看栈顶对象
 a.peek()
//移除栈顶对象
 a.pop()
// 添加对象
 a.push()
//大小
 a.size()
```



## Queue

```java
// Queue是一个interface
//一个 implementation 是linkedlist
//创建
Queue
Queue<Integer> a = new LinkedList<>();
//判断是是否为空
a.isEmpty();

Queue<int[]> a;

```

<img src="https://ae01.alicdn.com/kf/H0a372fea165f41c190bdec2f53b37abei.png" alt="image.png" title="image.png" />

## Deque

<img src="https://inews.gtimg.com/newsapp_ls/0/14047110077/0" alt="image.png" title="image.png" />



```java
Deque<Integer>  = new LinkedList<>();
// Add at the last
 deque.add("Element 1 (Tail)");
  
 // Add at the first
deque.addFirst("Element 2 (Head)");
  
 // Add at the last
 deque.addLast("Element 3 (Tail)");
  
  // Add at the first
 deque.push("Element 4 (Head)");
  
// Add at the last
deque.offer("Element 5 (Tail)");
  
// Add at the first
 deque.offerFirst("Element 6 (Head)");

// We can remove the first element
 // or the last element.
deque.removeFirst();
deque.removeLast();


```

![image-20211028204509410](C:\Users\Mrcao\AppData\Roaming\Typora\typora-user-images\image-20211028204509410.png)

## map

```java

map相当于一个函数，key为x, value为y；一个x只能对应一个y，但是一个y可以对应多个x。
如果想要用map表示同构函数，也就是一一对应的函数，那就需要一个y也对应一个x。即从y对x建立一个map即可。
//创建
Map<Character, Character> a = new HashMap<>();
void clear();// remove all mapping
boolean containsKey(Object key); //return true if key in map
boolean isEmpty() //
V get(Object key); // return key'value
V getOrDefault(Object key, V defaultvalue)//存在则返回对应value，否则返回defaultvalue
K keySet();//得到keys
V values();//得到values
put(K key, V val); // put in map
int size(); // return the number of key-value pairs

```

## Set

```java
//创建
Set<Integer> set = new HashSet<>();
boolean isEmpty();
int size();
boolean contains();// 是否包含某一值
boolean add(); // 添加
Object toArray();

//set中不存在顺序，要得到其中的
```

## Heap / PriorityQueue

```java
//initiate 和queue的操作一模一样。
Queue<Integer> a = new PriorityQueue<>();
//add
offer(E e);
//remove
poll();
//转化为array
toArray();
//查看
peek();

//大顶堆的实现
Queue<Integer> b = new PriorityQueue<>((x, y) -> (y-x));

```

## Integer



Integer.parseInt(s)与Integer.valueOf(s)的区别详解（https://blog.csdn.net/u010502101/article/details/79162587）

```java
Integer.parseInt(String s);
//Parses the string argument as a signed decimal integer.将s解析为有符号的整数，转化为int
Integer.valueOf(String s)
//转化为intteger
```



## String

###### Java String字符串总结https://www.jianshu.com/p/aeb7799ba09f

```java
char charAt(int index);// return the char value
int length();
boolean isEmpty();
char[] toCharArray();//转换为character 列表
String.valueOf(num)//int2str 将其他类型的序列转换为string
Integer.valueOf(string)// 将其他类型的序列转换为Integer
//字符串切片
s.substring(int start, int end)// 得到s的子序列
//字符串拼接，虽然String不能更改，但是可以拼接
s.substring(n, s.length()) + s.substring(0, n);
s.substring(int start);
s.trim()；//去除String两边的空格
    
s.split(String regex)
//Splits this string around matches of the given regular expression.
//String里面的内容可以分为空格和非空格
int i = s.length() - 1;
while(i >= 0 && s.charAt(i) != ' ') i--; //when i = -1 or character equals space，跳出\\循环。
while(i >= 0 && s.charAt(i) == ' ') i--; //when i = -1 or character equals non-space，跳出循环
```

```java
//字符串遍历
String res = "";
for (int i = n; i < s.length(); i ++) {
    res += s.charAt(i);
}

for (int i = 0; i < n; i ++) {
    res += s.charAt(i);
}

//或者另一种方法，当i>s.length时就从0重新开始遍历，直到n结束

for (int i = n; i < s.length() + n; i++) {
    res += s.charAt(i%s.length());
}
```

```java
//字符串切片
s.substring(n, s.length()) + s.substring(0, n);
```



#### StringBuilder

String是不可变字符串，StringBuffer和StringBuilder是长度可变的字符串，区别是前者是线程安全的，后者是线程不安全的，同样后者的效率也会更高。

```java
//build
StringBuilder str = new StringBuilder(CharSequece seq);
StringBuilder str = new StringBuilder(String str);

//append
str.append(object o);
//2str
str.charAt(int index);
str.deleteCharAt(int index);
str.delete(int start, int end);
str.toString();
str.capacity();
str.indexOf(String str);
```

#### Character

```java
//使用单引号''，而string则是使用双引号""

```



## loop

```java
// 用index进行循环
for (int i = 0; i < 10; i++) ;
//注意循环的起止点， i = 0, 1, 2, ... , 9共10次
// 用值进行循环
for (int i: range(5)) ;

```



## 求一列正数的最大值

```java
public int max(int[] nums) {
    int maxNum = 0;
    for (int num: nums) {
        maxNum = Math.max(num, maxNum);
    }
    return maxNum;
}
```

## 将str，array转化为map的方法

```java
Map<Character, Integer> map = new HashMap<>();
for (char c: s.toCharArray()) {
    map.put(c, map.getOrDefault(c, 0)+1);
}
```



## array 排序

```java
// 函数声明
public static void sort(int[] a);
//使用
int[] a = new int[5];
Arrays.sort(a);
```

## 中间元素

```java
int lo;
int hi;
int mid = lo + (hi-lo)/2这里得到的是中间靠左位置的index。
```

## 将一串char转化为set



```java
char[] letters;
int[] set = new int[26];
for (char c: letters) {
    set[c-'a'] = 1;
}
```



### charIndexArray

```java
//返回首个出现次数为1的字符。
int[] map = new int[26];
for (char c: str.toCharArray()) {
    map[c - 'a'] += 1;
}

for (char c: str.toCharArray()) {
    if (map[c - 'a'] == 1) return c;
}


```



## switch

The body of a switch statement is known as a switch block. A statement in the switch block can be labeled with one or more case or default labels. The switch statement evaluates its expression, then executes all statements that follow the matching case label.

differences from if-then-else:

An if-then-else statement can test expressions based on ranges of values or conditions, whereas  a switch statement tests expressions based only on a single integer, enumerated value.

```java
switch (month) {
            case 1:  monthString = "January";
                     break;
            case 2:  monthString = "February";
                     break;
            case 3:  monthString = "March";
                     break;
            case 4:  monthString = "April";
                     break;
            case 5:  monthString = "May";
                     break;
            case 6:  monthString = "June";
                     break;
            case 7:  monthString = "July";
                     break;
            case 8:  monthString = "August";
                     break;
            case 9:  monthString = "September";
                     break;
            case 10: monthString = "October";
                     break;
            case 11: monthString = "November";
                     break;
            case 12: monthString = "December";
                     break;
            default: monthString = "Invalid month";
                     break;
        }
```

## Judge even  & odd

https://stackoverflow.com/questions/14905643/what-does-this-boolean-number-1-0-mean

只有奇数尾部才能为1，&表示位运算。所以奇数才会等于1，偶数则为0.

```java
private static boolean isEven(int number)
{
    return (number & 1) == 0;
}
```



## Mathematical operation

```java
//rounding
a/b 
// remainder
a%b
// divide
(double) a/b
// maximun minimun
Math.max()
Math.min()
//absolute value
Math.abs()
```



## Median

```java
//靠左的中位数a = (r-l)/2
//靠右的中位数b = (r-l+1)/2
//要注意array的范围是[l, r]，所以长度其实为r-l+1.这个是非常重要的。
//无论长度是奇还是偶，都可以通过靠左中位数和靠右中位数来求解。

int a = (r - l)/2;
int b = (r - l +1)/2;
int mid = (arr[a] + arr[b])/2
```



## 将一列数字，变为一个整数

```java
//nums = [1, 2, 3];
//res = 123;
public int turnNum(int[] nums) {
    int cur = 0;
    for (int num: nums) {
        cur = cur*10 + num;
    }
    return cur;
}

```



## 取等

分基本数据类型 和 引用数据类型。基本数据类型可以直接使用==，而引用数据类型则需要使用equals



## 循环数组

```java
//plusOne 长度为length的数组上的循环数组。求index对应的下一个index
public int plusOne(int x, int length) {
    if (x == length - 1) return 0;
    return x + 1;
}

//取余,当i = nums.length的时候，返回的结果是0，从而就很完美。
int i = i % nums.length;



```

