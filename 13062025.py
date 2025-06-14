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


"""class Student:
    _name = None
    _roll = None
    _branch = None
    def __init__(self,name,roll,branch):
        self._name = name
        self._roll = roll
        self._branch = branch
    def _displayinfo(self):
        print("Roll No:",self._roll)
        print("Branch:",self._branch)
class New(Student):
    def __init__(self,name,roll,branch):
        Student.__init__(self,name,roll,branch)
    def displaydetails(self):
        print("Name:",self._name)
        self._displayinfo()
obj = New("Aditya","TVMS4351","Data Science")
obj.displaydetails()"""


# Example of duck typing in Python
"""class Duck:
    def quack(self):
        print("Quack! Quack!")
class Person:
    def quack(self):
        print("I am quacking like a duck!)")
duck = Duck()
person = Person()
duck.quack()
person.quack()"""



"""class Bird:
    def fly(self):
        print("I can fly")
class Airplane:
    def fly(self):
        print("Airplane flies in sky with fuel")
class Fish:
    def swim(self):
        print("Fish swims in sea!")
for obj in Bird(), Airplane(), Fish():
    obj.fly()"""



"""class MyClass:
    def sum(self,a=0,b=0,c=0):
        s=0
        if a!=0 and b!=0 and c!=0:
            s=a+b+c
        elif a!=0 and b!=0:
            s=a+b
        elif a!=0:
            s=a
        else:
            s=0
        return s
m = MyClass()
print(m.sum(1,2,3))"""



"""class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self,other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self,scalar):
        return Vector(self.x * scalar, self.y * scalar)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * 3
print(v3)  # Output: Vector(6, 8)
print(v4)  # Output: Vector(-2, -2)
print(v5)  # Output: Vector(6, 9)
print(v1)  # Output: Vector(2, 3)"""



"""class Animal:
    def speak(self):
        print("Animal mkes a sound")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(Animal):
        print("Cat meows")

animal = Animal()
cat = Cat()
dog = Dog()
animal.speak()
dog.speak()
cat.speak()"""



