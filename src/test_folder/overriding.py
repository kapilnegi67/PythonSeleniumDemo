#  parent class
class Parent():

    # Constructor
    def __init__(self):
        self.value = "Inside Parent"
        
    # Parent's show method
    def show(self):
        print(self.value)

#  child class
class Child(Parent):
    
    # Constructor
    def __init__(self):
        self.value = "Inside Child"
        
    # Child's show method
    def show(self):
        print(self.value)


# create object
obj1 = Parent()
obj2 = Child()

obj1.show()
obj2.show()
