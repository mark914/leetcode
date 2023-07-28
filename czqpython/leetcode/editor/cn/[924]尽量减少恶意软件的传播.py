# 给出了一个由 n 个节点组成的网络，用 n × n 个邻接矩阵图 graph 表示。在节点网络中，当 graph[i][j] = 1 时，表示节点 i 能够
# 直接连接到另一个节点 j。 
# 
#  一些节点 initial 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传
# 播将继续，直到没有更多的节点可以被这种方式感染。 
# 
#  假设 M(initial) 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。 
# 
#  如果从 initial 中移除某一节点能够最小化 M(initial)， 返回该节点。如果有多个节点满足条件，就返回索引最小的节点。 
# 
#  请注意，如果某个节点已从受感染节点的列表 initial 中删除，它以后仍有可能因恶意软件传播而受到感染。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
# 输出：0
#  
# 
#  示例 2： 
# 
#  
# 输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
# 输出：0
#  
# 
#  示例 3： 
# 
#  
# 输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
# 输出：1
#  
# 
#  
# 
#  提示： 
#  
# 
#  
#  n == graph.length 
#  n == graph[i].length 
#  2 <= n <= 300 
#  graph[i][j] == 0 或 1. 
#  graph[i][j] == graph[j][i] 
#  graph[i][i] == 1 
#  1 <= initial.length <= n 
#  0 <= initial[i] <= n - 1 
#  initial 中所有整数均不重复 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 👍 69 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def minMalwareSpread(self, graph, initial):
        """
        :type graph: List[List[int]]
        :type initial: List[int]
        :rtype: int
        """
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()