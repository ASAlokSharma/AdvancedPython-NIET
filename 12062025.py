"""a=5
b=a.__add__(3)
print(b)
"""

"""
#Examples of using magic methods

# using + operator
num = 5
x = num + 3
print(x)
# using __add__ method
num = 5
x = num.__add__(3)
print(x)
#using + operator with string
a= '10'
b = a + '5'
print(b)
# using __add__ method with string
a = '10'
b = a.__add__('5')
print(b)"""


"""
# Define a custom class to represent a mass and then use the __add__ magic method to define how to add two instances of this class to add kilogrm and gram properly
class Mass:
    def __init__(self, kg=0, g=0):
        self.kg = kg + g // 1000
        self.g = g % 1000
    def __add__(self, other):
        total_kg = self.kg + other.kg
        total_g = self.g + other.g

        if total_g>=1000:
            total_kg += total_g // 1000
            total_g = total_g % 1000
        return Mass(total_kg,total_g)
    def __repr__(self):
        return f"{self.kg} kg {self.g} g"
# Example usage
mass1 = Mass(2, 500) 
mass2 = Mass(1, 800)  
mass3 = mass1 + mass2  
print(mass3) 
mass4 = Mass(2, 500)
mass5 = Mass(3,450)
mass6 = mass4 + mass5
print(mass6) 
"""


# Define a custom class to represent a distance(Km,m) and then use the __add__ magic method to define how to add two instances of this class to add distance in km and m properly
"""class Distance:
    def __init__(self, km=0, m=0):
        self.km = km + m // 1000
        self.m = m % 1000

    def __add__(self, other):
        total_km = self.km + other.km
        total_m = self.m + other.m

        if total_m >= 1000:
            total_km += total_m // 1000
            total_m = total_m % 1000
        return Distance(total_km, total_m)

    def __repr__(self):
        return f"{self.km} km {self.m} m"
    
t1 = Distance()
t1.__add__(Distance(2, 500))  # This will not change t1, it just returns a new Distance object
# Example usage
distance1 = Distance(2, 500)
distance2 = Distance(1, 800)
distance3 = distance1 + distance2
print(distance3)  """


# Define a custom class to represent a  in month and year and then use the __add__ magic method to define how to add two instances of this class to add month and year properly
"""class Time:
    def __init__(self, years=0, months=0):
        self.years = years + months // 12
        self.months = months % 12

    def __add__(self, other):
        total_years = self.years + other.years
        total_months = self.months + other.months

        if total_months >= 12:
            total_years += total_months // 12
            total_months = total_months % 12
        return Time(total_years, total_months)

    def __repr__(self):
        return f"{self.years} years {self.months} months"
    # Example usage
time1 = Time(2, 6)  # 2 years and 6 months
time2 = Time(1, 8)  # 1 year and 8 months
time3 = time1 + time2  # Adding the two Time objects
print(time3)  # Output: 4 years 2 months"""


# compare the marks of two students using magic methods
"""class Student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __gt__(self,other):
        r1 = self.m1 + self.m2
        r2 = other.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False
s1 = Student(50,60)
s2 = Student(70,80)
if s1 > s2:
    print("s1 is greater than s2 by",s1.m1 + s1.m2 - (s2.m1 + s2.m2),"marks")
else:
    print("s2 is greater than s1 by",s2.m1 + s2.m2 - (s1.m1 + s1.m2),"marks")"""



"""
import math
class Fraction:
    def __init__(self, num, deno):
        # Initialize numerator and denominator, then simplify the fraction
        self.num = num
        self.deno = deno
        self.simplify()

    def simplify(self):
            # Simplify the fraction using greatest common divisor (GCD)
            gcd = math.gcd(self.num, self.deno)
            self.num //= gcd
            self.deno //= gcd

    def __add__(self, other):
            # Add two fractions using the formula: a/b + c/d = (ad + bc)/bd
            new_num = self.num * other.deno + other.num * self.deno
            new_deno = self.deno * other.deno
            return Fraction(new_num, new_deno)

    def __eq__(self, other):
            # Check if two fractions are equal by cross-multiplying
            return self.num * other.deno == self.deno * other.num

    def __lt__(self, other):
            # Check if this fraction is less than another by cross-multiplying
            return self.num * other.deno < self.deno * other.num

    def __repr__(self):
            # String representation of the fraction
            return f"{self.num}/{self.deno}"

# Example usage
f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
f3 = f1 + f2
print(f3)  # Output: 5/6"""


"""class MyClass:
    def __init__(self, value):
        self.value = value

def print_value(self):
    print(f"The Value is : {obj.value}")
obj = MyClass(10)
print_value(obj)  # Output: The Value is : 10"""



# Define a class Person and another class Greeting. The greetng class should have a method that takes a person object and prints personalized greeting message.
"""class Person:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f"Person({self.name})"
class Greeting:
    def greet(self, person):
        print(f"Hello, {person.name}! Welcome to our program.")
# Example usage
person = Person("Garvit Rana")
greeting = Greeting()
message = greeting.greet(person)  # Output: Hello, Garvit Rana! Welcome to our program.
person = Person("Ishanvi Rajput")
greeting = Greeting()
message = greeting.greet(person)  # Output: Hello, Ishanvi Rajput! Welcome to our program."""



"""class MyClass:
    def __init__(self, value):
        self.value = value
def create_object(value):
    return MyClass(value)
obj = create_object(10)
print(f"The Value is : {obj.value}")  # Output: The Value is : 10"""



# Define a class rectangle that reresent a rectangle with width and height. The class should have a method that takes another retangle object and returns a new rectangle object that represents the union of the two rectangles.
class Rectangle:
    def __init__(slef,width,height):
        slef.width = width
        slef.height = height
    def area(self):
        return self.height * self.width
    def combine(self,other):
        new_area = self.area() + other.area()
        new_width = self.width
        new_height = new_area / new_width
        return Rectangle(new_width, new_height)
    def __repr__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
# Example usage
rect1 = Rectangle(4, 5)  # Rectangle with width 4 and height 5
rect2 = Rectangle(3, 6)  # Rectangle with width 3 and height 6
rect3 = rect1.combine(rect2)  # Combine the two rectangles
print(rect3)  # Output: Rectangle(width=4, height=9.5)
