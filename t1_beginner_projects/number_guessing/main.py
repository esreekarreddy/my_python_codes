from art import logo
from random import randint

print(logo)

computer_choice = randint(1,100)
print("Weclome to number guessing game...")
print("I'm thinking of a number between 1 and 100")

def guess(choices):
	game_over = False
	while not game_over and choices > 0:
		print(f"You have {choices} attempt(s) remaining to guess the number")
		user_choice = int(input("Make a guess: "))
		if user_choice > computer_choice:
			print("Too high, guess again.")
			choices -= 1
		elif user_choice < computer_choice:
			print("Too low, guess again.")
			choices -= 1
		else:
			print(f"You gussed correct, the answer was {computer_choice}")
			game_over = True
	if choices == 0:
		print("Game over, you lost")

difficulty_level = input("Choose your difficulty level (easy) or (hard): ")
if difficulty_level == "easy":
	choices = 10
	guess(choices)
elif difficulty_level == "hard":
	choices = 5
	guess(choices)
else:
	print("Enter a valid choice, game over.")