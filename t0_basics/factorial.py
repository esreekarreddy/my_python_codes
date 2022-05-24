value = int(input("Enter the value for which you want to calculate factorial? "))
result = 1

if value < 0:
    print("No factorial for negative numbers.")
elif value == 0 or value == 1:
    print(f"Fatorial of {value} is 1.")
else:
    for value1 in range(1, value+1):
        result *= value1
    print(f"Fatorial of {value} is {result}.")
