class Person:
    w = ''
    s = ''
    def __init__(self, walk, speak):
        self.w = walk
        self.s = speak
class Tomas(Person):
    w = ''
    s = ''
    def __init__(self, walk, speak):
        self.w = walk
        self.s = speak
obj1 = Tomas('walk', 'speak')
obj2 = Person('walk', 'speak')
print(obj1.w)
print(obj1.s)
