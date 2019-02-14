
from collections.abc import Iterable
from collections.abc import Iterator
#判断是否可以迭代

# 列表
print(isinstance([1,2], Iterable))
# 元组
print(isinstance((1,2), Iterable))
# 字典
print(isinstance({1,2}, Iterable))
# 字符串
print(isinstance("abc", Iterable))
# 生成器
g=(x for x in range(10))
print(isinstance(g, Iterable))
# 整数
print(isinstance(100, Iterable))



# 判断是否是迭代器

from collections.abc import Iterable
# 生成器
g=(x for x in range(10))
print(isinstance(g, Iterator))
# 列表
print(isinstance([1,2], Iterator))
# 字典
print(isinstance({1,2}, Iterator))
# 字符串
print(isinstance("abc", Iterator))
# 整数
print(isinstance(100, Iterator))