from collections import deque
class MinStack:
    def __init__(self):
        self.stack = deque()
        self.minStack = deque()
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack:
            self.minStack.append(val)
        else:
            minVal = min(self.minStack[-1], val)
            self.minStack.append(minVal)
    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


def print_result(funs, paras):
    res = []
    obj = None
    for i, (f, p) in enumerate(zip(funs, paras)):
        if i == 0:
            res.append(obj)
            obj = eval(f)(*p)
        else:
            res.append(getattr(obj, f)(*p))
    print(res)

def print_result(funs, paras):
    res = [None]
    obj = eval(funs[0])(*paras[0])
    for f, p in zip(funs[1:], paras[1:]):
        res.append(getattr(obj, f)(*p))
    print(res)

def testFunc(func, test, test_res):
    for t, t_r in zip(test, test_res):
        assert func(t) == t_r, f'{t}'
    print('pass successful!')
if __name__ == '__main__':
    f = ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
    s = [[], [-2], [0], [-3], [], [], [], []]
    print_result(f, s)