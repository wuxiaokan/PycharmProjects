from .test2 import Q


class B(Q):
    def __init__(self):
        print(self.b)

class C():
    a = 2
    # def __init__(self):
    #     print("C")
    #     self.num = 1
    def foo(self):
        print(self.a)

class D(B,C):
    # def __init__(self):
    #     # super().__init__()
    #     # super(B,self).__init__()
    #     # super(D,self).__init__()
    #     print("D")
    def bar(self):
        print(self.a)

d = D()
# print(d.num)
# print(d.a)
# d.foo()
d.bar()