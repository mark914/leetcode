class Solution:
    def countPairs(self, nums, k) -> int:
        def helper(indexs):
            res = []
            path = []

            def dfs(startIndex):
                if len(path) == 2 and (path[0]*path[1])%k == 0:
                    res.append(path[:])
                if startIndex == len(indexs):
                    return
                for i in range(startIndex, len(indexs)):
                    path.append(indexs[i])
                    dfs(i + 1)
                    path.pop()
            dfs(0)
            return res

        dic = dict()
        for i, num in enumerate(nums):
            dic[num] = dic.get(num, []) + [i]
        res = 0
        for key in dic.values():
            if len(key) >= 2:
                res += len(helper(key))
        return res

if __name__ == "__main__":
    s = Solution()
    nums = [3, 1, 2, 2, 2, 1, 3]
    k = 2
    s.countPairs(nums,k)