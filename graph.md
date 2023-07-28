

图遍历和回溯算法之间之间的区别

### 图论基础

https://labuladong.gitee.io/algo/2/19/35/

#### 图遍历和回溯的区别

这个 `onPath` 数组的操作很像 [回溯算法核心套路](https://labuladong.gitee.io/algo/4/29/110/) 中做「做选择」和「撤销选择」，区别在于位置：回溯算法的「做选择」和「撤销选择」在 for 循环里面，而对 `onPath` 数组的操作在 for 循环外面。

在 for 循环里面和外面唯一的区别就是对根节点的处理。

```java
void traverse(TreeNode root) {
    if (root == null) return;
    System.out.println("enter: " + root.val);
    for (TreeNode child : root.children) {
        traverse(child);
    }
    System.out.println("leave: " + root.val);
}

void traverse(TreeNode root) {
    if (root == null) return;
    for (TreeNode child : root.children) {
        System.out.println("enter: " + child.val);
        traverse(child);
        System.out.println("leave: " + child.val);
    }
}

```

前者会正确打印所有节点的进入和离开信息，而后者唯独会少打印整棵树根节点的进入和离开信息。

为什么回溯算法框架会用后者？因为回溯算法关注的不是节点，而是树枝

关键：

- 关注树枝，而不关注根节点的，就使用在child中的结果。
- 关注每一个节点的，就是使用在最开始的结果。



#### marked数组的使用

只有当数组中存在环，正常遍历可能会重复经过某一个位置的时候，才需要用marked进行辅助。

如果是有向无环图，那就不需要marked数组，因为根本不会出现重复遍历的情况。



##### ex1

[797. 所有可能的路径](https://leetcode-cn.com/problems/all-paths-from-source-to-target/)

回溯的关键是操作然后撤销的操作，也就是在进入下一个child之前，先从上一个child中出来，下面这里传入的是path+[i]，path并没有改变，所以也就不需要撤销的操作。然后又因为是有向无环图，递归一定是有限的，所以也可以不用return。

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans=[]
        end=len(graph)-1
        
        def dfs(node,path,output):
            if node==end:
                output.append(path)
            
            for i in graph[node]:
                dfs(i,path+[i],output)
            
        dfs(0,[0],ans)
        return ans 
```

这里是只关注child，没有关注根节点。有进入所有节点，然后出来的操作。最后在向path中添加第一个节点就可以了。

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def traverse(s):  
            if s == len(graph) - 1:
                res.append(path[:])
                return 
            for child in graph[s]:
                path.append(child)
                traverse(child)
                path.pop()
        res = []
        path = []
        path.append(0)
        
        traverse(0)
        return res
```



这里是在进入每一个节点进行操作，出节点的地方撤销操作。这其中也包含根节点。但是在到达结果的时候，有一个return，得到结果，停止遍历。此时就没办法让path.pop()，因此要在这里让path.pop()

```python
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def traverse(s):
            path.append(s)
            if s == len(graph) - 1:
                res.append(path[:])
                path.pop()
                return 
            for child in graph[s]:
                traverse(child)
            path.pop()
        res = []
        path = []
        traverse(0)
        return res
```

#### 图遍历框架

将判断是否遍历过，return，放在函数开头。**因为一般 return 语句都是 base case，集中放在一起可以让算法结构更清晰**。

```java
/* 图遍历框架 */
boolean[] visited;
void traverse(Graph graph, int v) {
    // 防止走回头路进入死循环
    if (visited[v]) return;
    // 前序遍历位置，标记节点 v 已访问
    visited[v] = true;
    for (TreeNode neighbor : graph.neighbors(v))
        traverse(graph, neighbor);

```

也可以将判断是否遍历过放在子节点中。这里你需要保证调用traverse(v)的时候，v是没有遍历过的。

```java
/* 图遍历框架 */
boolean[] visited;
void traverse(Graph graph, int v) {
    // 前序遍历位置，标记节点 v 已访问
    visited[v] = true;
    for (int neighbor : graph.neighbors(v)) {
        if (!visited[neighbor]) {
            // 只遍历没标记过的相邻节点
            traverse(graph, neighbor);
        }
    }
}
```

关键：

- 放在函数开头，还是放在循环中，主要的判断依据是是否对根节点有用。也就是是否要对函数调用的时候进入的那个节点起作用。
- 放在循环里就没法对函数调用的时候那个节点起作用了。

#### 二分图判定

https://labuladong.gitee.io/algo/2/19/37/

**给你一幅「图」，请你用两种颜色将图中的所有顶点着色，且使得任意一条边的两个端点的颜色都不相同，你能做到吗**？

如何存储电影演员和电影之间的关系？

如果用哈希表存储，需要两个哈希表分别存储「每个演员到电影列表」的映射和「每部电影到演员列表」的映射。

但如果用「图」结构存储，将电影和参演的演员连接，很自然地就成为了一幅二分图。



关键：

- 如果是二分图，那就能一次将graph染色成功，否则就不是。
- 对没遍历过的节点进行染色，对遍历过的节点检查染色成果



#### 拓扑排序

有向无环图：

<img src="https://inews.gtimg.com/newsapp_ls/0/14792731383/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />

<img src="https://inews.gtimg.com/newsapp_ls/0/14792736193/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />

每一次输出没有前驱顶点的顶点， 也就是没有输入到它的顶点数为0。输出之后在图中抹去这些节点，然后在剩下没有前驱节点的顶点继续进行输出。

<img src="C:\Users\Mrcao\AppData\Roaming\Typora\typora-user-images\image-20220424152923173.png" alt="image-20220424152923173" style="zoom:50%;" />

<img src="C:\Users\Mrcao\AppData\Roaming\Typora\typora-user-images\image-20220424153118556.png" alt="image-20220424153118556" style="zoom:50%;" />

<img src="https://inews.gtimg.com/newsapp_ls/0/14792770755/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />

#### 图不连通怎么办

<img src="https://inews.gtimg.com/newsapp_ls/0/14798324693/0.jiketuchuang.png" alt="image.png" title="image.png" />

#### 无权图的单元最短路算法

<img src="https://inews.gtimg.com/newsapp_ls/0/14798295329/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />



#### 有权图的单源最短路算法

cs61b

https://cs61b.bencuan.me/algorithms/shortest-paths/dijkstras-algorithm

和无权图不同之处在于， 经过顶点最少的路径并不是最短路径，需要看权重之和。

如果有条边的权重是负的，有负值圈（不考虑）

思路：

<img src="https://inews.gtimg.com/newsapp_ls/0/14798149672/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />

​	<img src="https://inews.gtimg.com/newsapp_ls/0/14798177933/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />

将v收进s的时候，v就会确定最短路径。

真正的最短路径必须只经过s中的顶点：

如果不经过s中顶点，说明存在比v更短的路径，并且它不再s中，这就产生了矛盾，因为路径是按照递增顺序产生的（距离小于v的顶点一定在它之前被收入s中了）

每次从dist里面，找没有没收进去的顶点的最小值，然后将dist最小的收进去（贪心）

增加一个v进入s，可能会影响另外一个顶点w的dist值



<img src="https://inews.gtimg.com/newsapp_ls/0/14798188187/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />

<img src="https://inews.gtimg.com/newsapp_ls/0/14798193982/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />

<img src="https://inews.gtimg.com/newsapp_ls/0/14798201538/0.jiketuchuang.png" alt="image.png" title="image.png" style="zoom:50%;" />

#### 多源最短路算法





使用python实现dijkstra方法：

表示图的方法有很多种，这里使用的是邻接矩阵

https://stackabuse.com/dijkstras-algorithm-in-python/



```python
class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
   def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0
    
        pq = PriorityQueue()
        pq.put((0, start_vertex))
    
        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)
    
            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D
```



```python
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        elapsedTime, graph, heap = [0] + [float('inf')] * n, defaultdict(list), [(0,k)]
        path = [-1] * (n+1)
        ## 建图
        for u, v, w in times:
            graph[u].append((v, w))
        ## 开始
        while heap:
            ## 将最小的时间拿出来
            time, node = heapq.heappop(heap)
            ## 查看它是否是最小的时间（如果是最小的时间，说明不用在进行更新了），dijkstra里面
            ## 如果进入closed set说明不用更新，和这里是一样的。因为这里只对不是最小的进行更新
            if time < elapsedTime[node]:
                elapsedTime[node] = time
                for v, w in graph[node]:
                    ## 同时对其它时间推进去
                    heapq.heappush(heap, (time+w, v))
                    path[v] = node
        print(path)
        mx = max(elapsedTime)
        return mx if mx < float('inf') else -1
```

