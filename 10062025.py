# # a=5
# # b=6
# # c=a+b
# # print(c)

# # Sum of 3 No.
# a = int(input("Enter first Number: "))
# b = int(input("enter second Number: "))
# c = int(input("Enter the third number: "))
# sum = a+b+c
# print(sum)

# If and else stetements
"""age = int(input("input your age please : "))
if age >=  18:
    print("Congratz! You are eligible to vote.")
else:
    print("Sorry! You can't vote.")"""

"""def findsum(a,b):
    result = a + b
    return result
x=5
y=7
z=findsum(x,y)
print(z)"""

"""def sum_num(num1,*num):
    result=num1
    for i in num:
        result +=i
    return result
r = sum_num(10,20,30)
print(f"The sum of number is: {r}")"""

"""def generate_report(name,marks,subject="Python"):
    average =  sum(marks)/len(marks)
    grade = "A" if average >= 90 else "B" if average >=75 else "C"
    print(f"{name}'s {subject} Report \nMarks : {marks} \nAverage : {average} \nGrade : {grade}\n")
generate_report("Aman Kumar Singh",[85,92,78])"""


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
class Student:
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
    print(row_format.format(*student.get_info()))