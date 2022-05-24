year = int(input("Enter the year you want to check: "))

# solution1
flag = None
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            flag = True
        else:
            flag = False
    else:
        flag = True
else:
    flag = False
if flag:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not leap year")

# solution 2
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# solution 3
if year % 400 == 0 and year % 100 == 0:
    print(f"{year} is a leap year")
elif year % 4 ==0 and year % 100 !=0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")