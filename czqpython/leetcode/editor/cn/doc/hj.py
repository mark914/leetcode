
def topKSmallest(nums, k):
    nums.sort()
    return nums[:k]


argu1 = input().strip().split(' ')
argu2 = input().strip().split(' ')

total, k = list(map(int, argu1))
nums = list(map(int, argu2))
if total >= k:
    res = topKSmallest(nums, k)
    print(res)




