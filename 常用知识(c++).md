### 代码结构

```c++
//函数定义在solution中，需要public等修饰词
class Solution 
{
    public:
    	int getFirst(vector<int>& nums, int target){}
    	int getLast(vector<int>& nums, int target){}
    	vector<int> searchRange(vector<int>& nums, int target) {}
};
```



### 初始化赋值

```c++
int left(0), right(nums.size() - 1);
```

### 逻辑语句

```c++
//while
while (condition) {
    statement;
}

//if
if (condition) {
    statement;
} else if {
    statement;
} else {
    statement;
}
//三目运算符
condition ? expression1 : expression2


// for语句
for (init-statement; condition; expression) {
    statement;
}
auto beg = v.begin();
for (/*空语句*/; beg != v.end() && *beg > 0; ++beg ) {
    ;
}
//范围for语句
for (declaration: expression) {
    statement;
}
```



### 常用数据类型

#### vector

```c++
//初始化方法
vector<T> v1;
vector<T> v2(v1);
vector<T> v2 = v1;
vector<T> v3{a,b,c}; vector<int>{1, 2};
//vector操作
v.empty();
v.size();
v.push_back(t);
v[n];
v1 = v2;

```

#### String

```c++
//初始化
string s1;
string s2(s1);
string s2 = s1;
string s3("value");
string s3 = "value";
string s4(n, 'c');

//操作
os << s;
getline(is, s);
s.empty();
s.size();
s[n];
s1 + s2;

```



### 注意事项

定义时需要声明类型

每句话后面都要加上分号";".



