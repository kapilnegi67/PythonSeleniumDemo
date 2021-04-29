# # Parent or Base class
#
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname
#
#     def printname(self):
#         print(self.firstname, self.lastname)
#
#
# # Simple Inheritence
# # Child class
# class Student(Person):
#   pass
#
# x = Student("Kapil", "Negi")
# y = Student("Steve", "Rogers")
# x.printname()
# y.printname()

# Multiple, Multilevel

class A:
    def __init__(self):
        print("Constructor of class A")
    
    def funcA(self):
        print("FuncA of Class A")

class B:
    def __init__(self):
        print("Constructor of class B")
    
    def funcB(self):
        print("FuncB of Class B")

class C:
    def __init__(self):
        print("Constructor of class C")
    
    def funcC(self):
        print("FuncC of Class C")


# Multiple Inheritance = > One child class has more than 1 parent class
# Multilevel Inheritance = > When parent class of a child is a child of some other parent class

# class D(B, A, C):
#     pass
#
# d_obj = D()
#
# d_obj.funcC()
# d_obj.funcA()
# d_obj.funcB()

class E(C):
    def __init__(self):
        print("Constructor of class E")
    
    def funcE(self):
        print("FuncC of Class E")

class F(E):
    def __init__(self):
        print("Constructor of class F")
        super().__init__()
    
    def funcF(self):
        print("FuncC of Class F")

my_obj = F()
my_obj.funcC()
my_obj.funcE()
my_obj.funcF()
