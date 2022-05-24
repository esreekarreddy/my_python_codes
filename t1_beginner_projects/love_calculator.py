print("Welcome to the love calculator...")
name1 = input("What is person 1 name?\n").lower()
name2 = input("What is person 2 name?\n").lower()

name = name1 + name2
t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")
true_value = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")
love_value = l + o + v + e

final_value = int(str(true_value) + str(love_value))

if final_value < 10 or final_value > 90:
    print(f"Your score is {final_value}, you go together like coke and mentos.")
elif 40 <= final_value <= 50:
    print(f"Your score is {final_value}, you are alright together.")
else:
    print(f"Your score is {final_value}.")
