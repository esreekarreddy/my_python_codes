import art
import os

def add(m, n):
    return m + n

def subtract(m, n):
    return m - n

def multiply(m, n):
    return m * n

def divide(m, n):
    return m / n

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
def calculator():

    print(art.logo)
    m = float(input("What's the first number? "))
    for i in operations:
        print(i)
    flag = False

    while not flag:
        operator = input("Pick your operator: ")
        n = float(input("What's the next number? "))
        operation_function = operations[operator]
        answer = operation_function(m, n)
        print(f"{m} {operator} {n} = {answer}")

        next = input("Do you want to use previous result for a new calculation(y) or go for a new calculation(n) or exit(z)? ")
        if next == 'y':
            m = answer
        elif next == "z":
            flag = True
            print("Program ends now.")
            exit()
        else:
            os.system("clear")
            calculator()

calculator()