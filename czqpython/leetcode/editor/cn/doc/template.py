from collections import Counter


class Solution:
    def sortChar(self, strs:str) -> str:
        # write code here
        nAlpha = []
        lst = []
        for idx, s in enumerate(strs):
            if s.isalpha():
                lst.append(s)
            else:
                nAlpha.append((s, idx))
        lst.sort(key=lambda x:x.lower())
        for (s, idx) in nAlpha:
            lst.insert(idx, s)
        return ''.join(lst)
def testFunc(func, test, test_res):
    for t, t_r in zip(test, test_res):
        assert func(t) == t_r, f'{t}'
    print('pass successful!')
if __name__ == "__main__":
    s = Solution()
    test = ["A Famous Saying: Much Ado About Nothing (2012/8)."]
    test_res = ["A aaAAbc dFgghh: iimM nNn oooos Sttuuuy (2012/8)."]
    testFunc(s.sortChar, test, test_res)


