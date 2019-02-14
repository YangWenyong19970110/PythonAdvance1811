# q1=[i for i in range(100)]
# print(q1)
# print(type(range(100)))
# q2=(i for i in range(100))
# print(next(q2),next(q2),next(q2))
# print(type(q2))
# for i in q2:
#     print(i)
# def fun():
#     yield 10
#     yield 20
#     yield 30
#     return "hello"
# reslut=fun()
# print(type(reslut))
# # for i in reslut:
# print(next(reslut))
# print(next(reslut))
# print(next(reslut))
# try:
#     print(next(reslut))
# except StopIteration as e:
#     print(e)

def fun(n):
    a, b =0,1
    yield a
    yield b

    count = 0
    while count<n:
        a, b = b, a + b
        yield b
        count +=1

result = fun(3)
for i in result:
    print(i)
while True:
    try:
        print(next(result))
    except StopIteration as e:
        print(e)
        break