"""def decor(add):
    def inner():
        result = add() # Existing function
        num3 = float(input("Enter number 3: "))
        result += num3


    return inner
@decor

def add():
    num1 = float(input("Enter number 1: "))
    num2 = float(input("Enter number 2: "))
    result = num1 + num2

    decor(add())

    print(result)
add()"""


"""from datetime import datetime
def not_during_night(func):
    def inner():
        if 7<= datetime.now().hour < 22:
            func()
        """


