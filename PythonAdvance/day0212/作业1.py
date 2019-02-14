class Person(object):
    name="ywy"

    def __init__(self,_age):
        self.age=_age
p1=Person(18)
p2=Person(20)
# 类可以操作类属性，不可以操作实例属性
print(Person.name)
# 实例可以操作实例属性，可以操作类属性
print(p1.age,p2.age)
print(p1.name,p2.name)
