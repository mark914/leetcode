class Solution:
    def maxChunksToSorted(self, arr) -> int:
        n = len(arr)
        maxOfLeft, minOfRight= [0] * n, [0] * n

        maxOfLeft[0] = arr[0]
        for i in range(1, n):
            maxOfLeft[i] = max(arr[i], maxOfLeft[i-1])

        minOfRight[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            minOfRight[i] = min(arr[i], minOfRight[i+1])

        res = 0
        for i in range(n-1):
            if maxOfLeft[i] <= minOfRight[i+1]:
                res += 1
        return res + 1

if __name__ == "__main__":
    s = Solution()
    s.maxChunksToSorted([2,1,3,4,4])