import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

image = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors? "))

if user_choice > 2 or user_choice < 0:
    print("You entered an invalid number, you lose")
else:
    computer_choice = random.randint(0, 2)
    print(f"You chose {image[user_choice]}")
    print(f"Computer chooses {image[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a tie.")
    elif user_choice == 0 and computer_choice == 2:
        print("You win.")
    elif user_choice == 1 and computer_choice == 0:
        print("You win.")
    elif user_choice == 2 and computer_choice == 1:
        print("You win.")
    else:
        print("You lose.")
