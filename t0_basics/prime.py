print("To print prime numbers please enter your range.....")
value1 = int(input("Enter your min range value: "))
value2 = int(input("Enter your mx range value: "))

for value in range(value1, value2):
    if value > 1:
        for x in range(2, value // 2 + 1):
            if value % x == 0:
                break
        else:
            print(f"{value} is a prime number")
