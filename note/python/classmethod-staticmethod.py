class ClassA():
    all_counter = 0 # all base class and subclass
    all_lis = []    
    counter = 5     # will be replaced by subclass
    lis = []
    
    def __init__(self, args):
        self.args = args

    def func(self, args):
        pass
    
    @staticmethod
    def func_static(args):
        pass
    
    @classmethod
    def func_class(cls, args):
        cls.all_counter += 1 # 实际上和 ClassA.all_counter += 1 是非常不一样的。 准确来说应该用 ClassA
        cls.all_lis.append(args) # 准确来说应该用 ClassA

        cls.counter += 1
        cls.lis.append(args)

class ClassA_1(ClassA):
    counter = 0
    lis = []
    pass
print('start')
o1 = ClassA(1)
o2 = ClassA_1(1)

o1.func_class(1)
import pdb; pdb.set_trace()
assert(o1.all_counter==1 and o2.all_counter==1)
assert(o1.counter==6 is not o2.counter==0)
assert((o1.all_lis is o2.all_lis) and o1.all_lis==[1])
assert(o1.lis==[1] and o2.lis==[])

o2.func_class(2)
print(o1.all_counter, o2.all_counter)
#assert(o1.all_counter==2 and o2.all_counter==2) # python 里面变量全是引用，是不可变int，引用到新的int了
assert(o1.counter==6 is not o2.counter==1)
assert((o1.all_lis is o2.all_lis) and o1.all_lis==[1,2]) # 引用：all_lis 指向的地址没变。
assert(o1.lis==[1] and o2.lis==[2])
print('end')
