from collections import deque
def inOrder(root):
    if not root:
        return []
    res = []
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        res.append(node.val)
        if not node.left:
            queue.append(root.left)
        if not node.right:
            queue.append(root.right)
    return res


def bubbleSort(nums):
    n = len(nums)
    if n <= 1: return nums
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == "__main__":
    nums = [4, 3, 2, 1]
    res = bubbleSort(nums)
    print(res)
