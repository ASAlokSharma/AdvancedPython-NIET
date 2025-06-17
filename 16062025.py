"""from time import sleep

# List of student names
students = ["Atul", "Bharat", "Chirag", "Dinesh", "Esha", "Firoz", "Gaurav", "Hina"]

def read():
    # Simulate reading data with a delay
    sleep(3)
    print("Reading done !")
    data = students
    # Infinite loop to keep the generator active
    while True:
        # Wait for a name to be sent to the generator
        name = (yield)
        # Check if the name is in the data
        if name in data:
            print("Found")
        else:
            print("Not found")

# Create the generator object
search = read()
print("Reading all data...")
# Start the generator (advance to the first yield)
next(search)
# Search for "Chirag" in the student list
search.send("Chirag")  # Output: Found
# Search for "Aman" in the student list
search.send("Aman")    # Output: Not found"""


"""import sys
l1 = [13,65,45,87,23,56,60,43,89]
for i in l1:
    print(i)

for i in l1:
    print(i)
print("for range:",sys  .getsizeof(l1))"""


"""list = [20,30,40,50,60,10,85,35,67,32,89]
iter_obj = iter(list)
print(iter_obj)
print(type(iter_obj))
print(next(iter_obj))"""


"""l = [2,5,2,9,1,6]
iter_obj1 = iter(l)
print(type(iter_obj1))
print("ID of iter_obj1:", id(iter_obj1))
iter_obj2 = iter(l)
print(type(iter_obj2))
print("ID of iter_obj2:", id(iter_obj2))"""


# making our own for loop using iter and next
"""l = [2, 5, 2, 9, 1, 6]
def my_for_loop(iterable):
    iterator = iter(iterable)
    try:
        while True:
            print(next(iterator))
    except StopIteration:
        pass
my_for_loop(l)"""


"""import sys
class PowerOfTwo:
    def __init__(self,max_val):
        self.limit = max_val
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.limit:
            result = self.current
            self.current = self.current*2
            return result
        else:
            raise StopIteration
n = int(input("Enter the limit: "))
iter_obj = PowerOfTwo(n)
for num in iter_obj:
    print(num)
print("Memory size of the iterator object:", sys.getsizeof(iter_obj))"""



"""class My_Range:
    def __init__(self,start=0,stop=None,step=1):
        self.start = start
        self.stop = stop
        self.step = step
    def __iter__(self):
        return My_Range_Iterator(self)
class My_Range_Iterator:
    def __init__(self,iterable_obj):
        self.iterable_obj = iterable_obj
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterable_obj.start <= self.iterable_obj.stop:
            result = self.iterable_obj.start
            self.iterable_obj.start += self.iterable_obj.step
            return result
        else:
            raise StopIteration
num = My_Range(1,10)
iter_obj = iter(num)
for n in iter_obj:
    print(n)"""



# ** GUI in Python **

# from tkinter import *
# window = Tk()
# window.title("My first GUI")

# Python tkinter hello world program
"""
from tkinter import *

win = Tk()
# Add your body
win.title("The VibeMedia")
def button_clicked():
    button.config(text="Good Job !",bg="Dark Green",fg="White")
button = Button(win, text="Click me", command=button_clicked)
Button.config(bg="Dark Blue", fg="White", font=("Figtree Bold", 24))
# def button_clicked():

#     print("Button clicked !")
# Button = Button(win,text="Click me",command=button_clicked)
# Label = Label(win, text="The VibeMedia", font=("Figtree Bold", 24))
# Label.config(bg="Dark Blue", fg="White")
# Label.pack(pady=150, padx=150)
Button.pack(padx=50,pady=50)
# Add your body 
win.mainloop()"""

import tkinter as tk
from tkinter import *
win = tk.Tk()
win.title("The VibeMedia")
win.geometry("800x200")
scale = tk.Scale(win, from_=0, to=100, orient=HORIZONTAL, length=500)
scale.pack()
win.mainloop()
