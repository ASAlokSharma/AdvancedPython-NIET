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
