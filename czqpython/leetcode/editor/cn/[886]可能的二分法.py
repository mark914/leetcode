# 给定一组 n 人（编号为 1, 2, ..., n）， 我们想把每个人分进任意大小的两组。每个人都可能不喜欢其他人，那么他们不应该属于同一组。 
# 
#  给定整数 n 和数组 dislikes ，其中 dislikes[i] = [ai, bi] ，表示不允许将编号为 ai 和 bi的人归入同一组。当可以用
# 这种方法将所有人分进两组时，返回 true；否则返回 false。 
# 
#  
# 
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 4, dislikes = [[1,2],[1,3],[2,4]]
# 输出：true
# 解释：group1 [1,4], group2 [2,3]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 3, dislikes = [[1,2],[1,3],[2,3]]
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：n = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 2000 
#  0 <= dislikes.length <= 10⁴ 
#  dislikes[i].length == 2 
#  1 <= dislikes[i][j] <= n 
#  ai < bi 
#  dislikes 中每一组都 不同 
#  
# 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 图 👍 157 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """

        def buildGraph(n, dislikes):
            graph = [0] * (n + 1)
            for i in range(1, n+1):
                graph[i] = []
            def addEdge(edge):
                v = edge[0]
                w = edge[1]
                graph[v].append(w)
                graph[w].append(v)
            for edge in dislikes:
                addEdge(edge)
            return graph
        def dfs(v):
            visited[v] = 1
            for c in graph[v]:
                if not visited[c]:
                    color[c] = 1 - color[v]
                    dfs(c)
                else:
                    if color[c] == color[v]:
                        self.res = False
                        return
        graph = buildGraph(n, dislikes)
        self.res = True
        visited = [0] * (n+1)
        color = [0] * (n+1)
        for i in range(1, n+1):
            if not visited[i] and self.res:
                dfs(i)
        return self.res
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()