"""class Apple_design:
    count = 0  # Class variable or static variable to count instances
    def __init__(self,cpu,ram): # Constructor with parameters
        self.cpu = cpu
        self.ram = ram
    def mobile(self,cpu,ram): # instance variable
        print("This is Apple mobile")
        print(self.cpu, self.ram)
        print(type(self))
# Above code is design of class
# Below code is instantiation of class
m1 = Apple_design(3.5, 8)
m2 = Apple_design(4.5, 16)

print(id(m1)) 
print(id(m2))
m1.mobile(3.5, 8)  # default constructor but now parameterized
m2.mobile(4.5, 16)  # default constructor but now parameterized
# This code defines a class `Apple_design` with a method `mobile`
# Output will show different memory addresses for m1 and m2
# and both will print "This is Apple mobile"""



"""# Example - Create class and objects
class Greeting:
    message = "Hello, World!"  # Class variable
    def say_hello(self):
        print(self.message)

    # Create an object
greet = Greeting()  # Object instantiation
# Call the method
greet.say_hello()  # Output: Hello, World!"""



"""# Example - Create a desing and obejct and access attributes like milage, speed, color
class Car:
    wheel = 4
    def __init__(self, Model, mileage, speed, color,year):
        self.Model = Model      # Instance variable
        self.mileage = mileage  # Instance variable
        self.speed = speed      # Instance variable
        self.color = color      # Instance variable
        self.year = year        # Instance variable

    def info(self):
        print(f"Vehicle Info: Model={self.Model}, Mileage={self.mileage}, Speed={self.speed}, Color={self.color}, Year={self.year}, Wheels={self.wheel}")
# Create an object of the Car class
my_car = Car("MG Astor", 15, 150, "White", 2023)  # Object instantiation
# Accessing attributes and calling method
my_car.info()  # Output: Vehicle Info: Model=MG Astor, Mileage=15, Speed=150, Color=White"""


"""#Example - Create a class and object with attributes like name, age and method to display them
class person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create an object of the person class
p1 = person("Alice", 30)  # Object instantiation
# Accessing attributes and calling method
p1.display()  # Output: Name: Alice, Age: 30"""


"""# Example - Employee of an office
class Employee:
    office_name = "Noida Institute of Engg & Technology"
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
    def display_info(self):
        print(f"Office: {self.office_name}\nEmployee Name: {self.name}\nDesignation: {self.designation}\n")
# Create an object of the Employee class
e1 = Employee("John Doe", "Software Engineer")  # Object instantiation
e2 = Employee("Jane Smith", "Data Scientist")  # Another object instantiation
e3 = Employee("Alice Johnson", "Project Manager")  # Yet another object instantiation
# Accessing attributes and calling method
e1.display_info(),e2.display_info(),e3.display_info()"""    


"""# Example - Even and odd number classification
class number:
    even = []
    odd  = []
    def __init__(self,num):
        self.num = num
        if num %2 == 0:
            number.even.append(num)
        else:
            number.odd.append(num)
N1 = number(21)
N1 = number(18)
N1 = number(65)
N1 = number(29)
N1 = number(54)
N1 = number(70)
print("even numbers are : ",number.even)
print("odd numbers are : ",number.odd)"""


# Example - Person Details
"""class person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable

    def display(self):
        print(f"Your name is {self.name} & Age is {self.age}")
# Create an object of the person class
p1 = person("Alice", 30)  # Object instantiation
# Accessing attributes and calling method
p1.display()  # Output: Your name is Alice & Age is 30"""


# Example - Student Class with Class Variable and Method
"""class Student:
    counter = 0
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.counter = Student.counter + 1
    def msg(self):
        print("Hello "+self.name + "!" + " You got", self.marks, "% marks")
        @classmethod
        def total_students(cls):
            return cls.counter
# Create objects of the Student class
s1 = Student("Dhruvika", 85)
s2 = Student("Aarav", 90)
s3 = Student("Yamika", 78)
# Accessing attributes and calling methods 
s1.msg()  # Output: Hello Dhruvika! you got 85 % marks"""


# Example - Math Operations using ststic methods
"""class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def subtract(a, b):
        return a - b
obj = MathOperations()  # Object instantiation
# Using static methods to perform operations
result_add = obj.add(10, 5)  # Output: 15
result_subtract = obj.subtract(10, 5)  # Output: 5
print(f"Addition Result: {result_add}")  # Output: Addition Result: 15
print(f"Subtraction Result: {result_subtract}")  # Output: Subtraction Result: 5"""
