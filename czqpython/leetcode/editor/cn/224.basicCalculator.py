from collections import deque
class Solution:
    def str2num(self, strs):
        res = 0
        for num in strs:
            res = res*10 + int(num)
        return res
    def calcultorOfPlusSub(self, strs):
        ## deal with plus and substract
        stack = deque()
        num = 0
        sign = '+'
        for i in range(len(strs)):
            c = strs[i]
            if c.isdigit():
                num = num*10 + int(c)
            if not c.isdigit() or i == len(strs) - 1:
                if sign == '+': stack.append(num)
                elif sign == '-': stack.append(-num)
                ## 重新开始记录num
                sign = c
                num = 0
        return sum(stack)

    def calcultorOfProduct(self, strs):
        ## deal with plus and substract
        stack = []
        num = 0
        sign = '+'
        for i in range(len(strs)):
            c = strs[i]
            if c.isdigit():
                num = num*10 + int(c)
            if not c.isdigit() or i == len(strs) - 1:
                if sign == '+': stack.append(num)
                elif sign == '-': stack.append(-num)
                elif sign == '*': stack[-1] = stack[-1] * num
                elif sign == '/': stack[-1] = int(stack[-1]/num)
                ## 重新开始记录num
                sign = c
                num = 0
        return sum(stack)


    def calcultorOfProductWithBrace(self, strs):
        ## deal with plus and substract
        def helper(strs):
            stack = []
            num = 0
            sign = '+'
            while strs:
                c = strs.pop(0)
                if c.isdigit():
                    num = num*10 + int(c)
                if c == '(':
                    num = helper(strs)
                if not c.isdigit() or len(strs) == 0:
                    if sign == '+': stack.append(num)
                    elif sign == '-': stack.append(-num)
                    elif sign == '*': stack[-1] = stack[-1] * num
                    elif sign == '/': stack[-1] = int(stack[-1]/num)
                    ## 重新开始记录num
                    sign = c
                    num = 0
                if c == ')':
                    break
            return sum(stack)
        return helper(list(strs))

    def calcultorOfProductWithBraceSpace(self, strs):
        ## deal with plus and substract
        def helper(strs):
            stack = []
            num = 0
            sign = '+'
            while strs:
                c = strs.pop(0)
                if c == " ": continue
                if c.isdigit():
                    num = num*10 + int(c)
                if c == '(':
                    num = helper(strs)
                if not c.isdigit() or len(strs) == 0:
                    if sign == '+': stack.append(num)
                    elif sign == '-': stack.append(-num)
                    elif sign == '*': stack[-1] = stack[-1] * num
                    elif sign == '/': stack[-1] = int(stack[-1]/num)
                    ## 重新开始记录num
                    sign = c
                    num = 0
                if c == ')':
                    break
            return sum(stack)
        return helper(list(strs))



    def testFuc(self, func, test, res):
        for t, r in zip(test, res):
            assert func(t) == r, f'{t} {func(t)}'
if __name__ == "__main__":
    s = Solution()
    strs1 = '3445'
    assert s.str2num(strs1) == 3445
    # test_cases = ['3445', '3+5', '4-5']
    # test_res = [3445, 8, -1]
    # s.testFuc(s.calcultorOfPlusSub, test_cases, test_res)
    # test_cases_product = ['3445', '3+5', '4-5', '3+5*2-1', '3+5/2-1']
    # test_res_product = [3445, 8, -1, 12, 4]
    # s.testFuc(s.calcultorOfProduct, test_cases_product, test_res_product)
    # test_cases_product3 = ['3445', '3+5', '4-5', '3+5*2-1', '3+5/2-1', '3+5*(2-1)']
    # test_res_product3 = [3445, 8, -1, 12, 4, 8]
    # s.testFuc(s.calcultorOfProductWithBrace, test_cases_product3, test_res_product3)
    # test_cases_product4 = ['3445', '3+5', '4-5', '3+5*2-1', '3+5/2-1', '3+5*(2-1)', '3 + 3', '(3 -4)*1 5']
    # test_res_product4 = [3445, 8, -1, 12, 4, 8, 6, -15]
    # s.testFuc(s.calcultorOfProductWithBraceSpace, test_cases_product4, test_res_product4)
    s.calcultorOfProductWithBraceSpace(" 2-1 + 2 ")



