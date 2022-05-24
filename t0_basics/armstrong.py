number = int(input("Enter the number you want to check if is it armstrong or not? "))
temp = number
result = 0
length = len(str(number))

# using for loop
for i in range(0,length):
    remainder = number % 10
    result += (remainder ** length)
    number //= 10
if result == temp:
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")


