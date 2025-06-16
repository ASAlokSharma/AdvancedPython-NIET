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


list = [20,30,40,50,60,10,85,35,67,32,89]
iter_obj = iter(list)
print(iter_obj)
print(type(iter_obj))
print(next(iter_obj))