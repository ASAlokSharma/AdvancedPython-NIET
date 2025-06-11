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



"""class Student:
    def __init__self():
        print("Default constructor called")
    def __init__(self,name,marks,age):
        self.name = name
        self.marks = marks
        self.age = age
        print("Parameterized constructor called")
    def show_info(self):
        print(f"Name: {self.name}\nMarks: {self.marks}\nAge: {self.age}")
    def __del__(self):
        print("Destructor called")
s2=Student("Dhruvika", 85, 20)  # Object instantiation with parameterized constructor
s2.show_info()  # Output: Name: Dhruvika, Marks: 85, Age: 20
s3=Student("Aarav", 90, 22)  # Another object instantiation with parameterized constructor
s3.show_info()  # Output: Name: Aarav, Marks: 90, Age: 22
del s2  # Destructor will be called for s2"""


# Example - Addition Class with Methods to Calculate and Display Sum
"""class Addition:
    first = 0
    second = 0
    answer = 0
    def __init__(self, f, s):
        self.first = f
        self.second = s
    def display(self):
        print("First number is: ", self.first)
        print("Second number is: ", self.second)
        print("Addition is: ", self.first + self.second)
    def calculate(self):
        self.answer = self.first + self.second
obj = Addition(1000,2000)  # Object instantiation
obj.calculate()  # Calculate the addition
obj.display()  # Display the results"""


# Example - Person Class with Instance Variables and Attribute Manipulation
"""class person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age    # Instance variable
person = person("Alice", 30)  # Object instantiation
# use getattr attribute to get the value of attribute
name = getattr(person, 'name')  # Accessing instance variable using getattr
print(f"Name: {name}")  # Output: Name: Alice
# use setattr attribute to set the value of attribute
setattr(person, 'age', 31)  # Modifying instance variable using setattr
print(f"Updated Age: {person.age}")  # Output: Updated Age: 31
# use hasattr attribute to check if the instance variable exists
has_name = hasattr(person, 'name')  # Checking if 'name' attribute exists
print(f"Has 'name' attribute: {hasattr(person, 'name')}")  # Output: Has 'name' attribute: True
# use delattr attribute to delete the instance variable
delattr(person, 'age')  # Deleting 'age' attribute using delattr
print(f"Has 'age' attribute after deletion: {hasattr(person, 'age')}")  # Output: Has 'age' attribute after deletion: False"""


# Rectangle area and perimeter calculation
"""class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
# Example usage
rect = Rectangle(5, 3)
print("Area of rectangle:", rect.area())  # Output: Area of rectangle: 15
print("Perimeter of rectangle:", rect.perimeter())  # Output: Perimeter of rectangle: 16"""


# Example - Student Class with Class and Instance Attributes
"""class Student:
    clg_name = "Noida Institute of Engg & Tech"  # Class attribute

    def __init__(self,std_id, name, age):
        self.std_id = std_id
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute
    def display_info(self):
        print(f"Student ID: {self.std_id}\nName: {self.name}\nAge: {self.age}\nSchool: {self.clg_name}\n")
# Example usage
s1 = Student("TVMS52374", "Raman Kumar Yadav", 20)
s2 = Student("TVMS52375", "Aman Kumar Singh", 21)
s3 = Student("TVMS52376", "Aarav Kumar", 22)
# Setting instance attributes for school name
s1.clg_name = "Noida Institute of Engg & Tech"
s2.clg_name = "Noida Institute of Engg & Tech"
s3.clg_name = "Noida Institute of Engg & Tech"
# Displaying student information
print("\n--- Students' Details ---\n")
s1.display_info()  # Output: Name: Raman Kumar Yadav, Age: 20, School: Noida Institute of Engg & Tech
s2.display_info()  # Output: Name: Aman Kumar Singh, Age: 21, School: Noida Institute of Engg & Tech
s3.display_info()  # Output: Name: Aarav Kumar, Age: 22, School: Noida Institute of Engg & Tech"""


# updated code to get output of above code in tabular form
"""class Student:
    clg_name = "Noida Institute of Engg & Tech"  # Class attribute

    def __init__(self, std_id, name, age):
        self.std_id = std_id
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def get_info(self):
        return [self.std_id, self.name, self.age, self.clg_name]

# Example usage
s1 = Student("TVMS52374", "Raman Kumar Yadav", 20)
s2 = Student("TVMS52375", "Aman Kumar Singh", 21)
s3 = Student("TVMS52376", "Aarav Kumar", 22)

students = [s1, s2, s3]

# Displaying student information in tabular form
print("\n--- Students' Details ---\n")
header = ["Student ID", "Name", "Age", "School"]
row_format = "{:<12} {:<20} {:<5} {:<30}"
print(row_format.format(*header))
print("-" * 70)
for student in students:
    print(row_format.format(*student.get_info()))"""