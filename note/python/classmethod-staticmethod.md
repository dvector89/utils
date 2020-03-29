先说结论：  
  
1. staticmethod: 几乎没有具体用途，尽量不要用。  
2. classmethod: 有继承，且函数需要改变或者访问的*类属性*是不同的时候。

# classmethod and staticmethod
``` python
def foo(args):
	pass

class ClassA():
    
    def __init__(self, args):
        pass

    def func(self, args):
        pass
	
	@staticmethod
    def func_static(args):
        pass
	
	@classmethod
    def func_class(cls, args):
        pass
```

类的普通函数、classmethod 以及 staticmethod，这三者的差别在于**函数的第一个参数不同**。    
## 分析差别
类的普通函数，包括构造函数，都是有 self 参数的。self 参数用来绑定类的实例（实际调用函数的是实例)。这些函数在运行的时候，需要通过实例来改变或者访问其状态。  

staticmethod 并不绑定类的实例，也不绑定类。其运行和类外的函数一样。相当于把函数的作用域从类外，放到了类内。这种函数其实完全可以放到类外。从使用角度，如果这个函数和类在运作上非常相关（甚至只与此类相关），则加 staticmethod 特性。（其实完全不必使用staticmethod的）

classmethod 要绑定类 cls 本身（实际调用函数的是类）。  

1. 如果没有类的继承，cls 永远是个固定的东西。那么并不需要将函数设置成 classmethod，可以设置成 staticmethod，甚至放到类外去。  
2. 假设有继承，那么该函数在运行的时候，就会判断到底是基类，还是其中某个继承类，并进行相应的绑定。在函数运行的过程中，假如需要改变或者访问的类属性是相同的，那也没有必要加 classmethod。  
3. 假设有继承，且在函数运行过程中，需要改变或者访问的类的属性是不同的，那么就需要加了。例如，不同的**类**函数、不同的**类**属性等。  


## classmethod 几种常见的用法
由“分析差别”中，可以看出 classmethod 只在有继承，函数在运行过程中需要改变或者访问类的属性不同的情况才有必要。以此，列出几种常见用法：


1. Python 的构造函数只有一个(不像 C++ 可以利用参数的不同，有多个构造函数)。可以在 classmethod 函数中调用 \_\_init\_\_，这样便相当于实现了类的多个构造函数。（注：没有继承也可以这么用，但往往并不需要 cls(因为 cls 是固定的)，用 staticmethod 就可以。但用staticmethod 实现多个构造函数，还不如直接在类外部调用特殊逻辑，然后处理好构造函数的参数，再调用构造函数。）   
2. 函数的运行需要类的属性。**类属性分两种，一种是被继承的，一种是被重载的**。单纯用被继承的 attribute，基类和继承类的 cls\.attribute 是同一个。被重载的 attribute，基类和继承类的 cls\.attribute 是两个不同的东西。需要注意这个差别。  
3. 外部逻辑代码需要判断类（尤其是在实例化对象之前）。
