# --------- Write a function to compute 5/0 and use try/except to catch the exceptions. ------

def divide():
    try:
        a = int(input("enter first number"))
        b = int(input("enter second number"))
        result = a / b
        print(a, "divided by", b, "is", result)
    except ZeroDivisionError:
        print("can't divide by zero")
    except ValueError:
        print("must use whole numbers")
divide()


