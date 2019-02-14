def fun1():
    a=1
    def fun2(b):
        return a+b
    return fun2


print(fun1, type(fun1))
print(fun1(), type(fun1()))
print(fun1()(6))
r1=fun1()
print(r1(6))