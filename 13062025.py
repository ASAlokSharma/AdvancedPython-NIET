# *INHERITANCE EXAMPLE*
# In this code, we define a Parent class with two methods and a Child class that inherits from Parent and adds two more methods.
"""class Parent:
    def feature1(self):
        print("Feature 1 of parent")
    def feature2(self):
        print("Feature 2 of parent")
class Child(Parent):
        def feature3(self):
            print("Feature 1 of child")
        def feature4(self):
            print("Feature 2 of child")
p=Parent()
c=Child()
p.feature1()
p.feature2()
c.feature3()
c.feature4()
c.feature1()
p.feature3()"""


"""class Shape:
    def __init__(self):
        self.colour = (0,0,0)
class Rectangle(Shape):
    def __init__(self,w,h):
        Shape.__init__(self)
        self.width = w
        self.height = h
    def area(self):
            return self.width*self.height
r1 = Rectangle(10,5)
print(r1.width)
print(r1.height)
print (r1.area())
print(r1.colour)"""


"""class Animal:
    name = ""
    def eat(self):
        print("I can eat")
class Dog(Animal):
    def display(self):
        print("My name is",self.name)
d1=Dog()
d1.name = "Jerry"
d1.display()"""


# Example using super keyword
"""class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        print(f"First name is {self.fname} and last name is {self.lname}.")
class Student(Person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)
        print("Inside student class init")
s=Student("Mohit","Kumar")"""


"""class Father:
    def __init__(self):
        print("Father class constructor")
    def show_father(self):
        print("Father class method")
class Son(Father):
    def __init__(self):
        print("Son class constructor")
    def show_son(self):
        print("Son class method")
class Grandson(Son):
    def __init__(self):
        print("Grandson class constructor")
    def show_grandson(self):
        print("Grandon class method")
g = Grandson()
g.show_grandson()
g.show_son()
g.show_father()"""