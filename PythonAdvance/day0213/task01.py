import types

class Person(object):

    def __init__(self,_name):
        self.name = _name

def setname(self,newname):
    self.name = newname

def getname(self):
    return self.name

p1 = Person("zzy")

p1.setn=types.MethodType(setname,p1)

p1.getn=types.MethodType(getname,p1)

p1.setn("zzy1")
print(p1.getn())