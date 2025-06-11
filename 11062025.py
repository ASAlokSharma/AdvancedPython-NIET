class Apple_design:
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
# and both will print "This is Apple mobile"