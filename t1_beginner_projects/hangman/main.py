import random
from ascii import logo, stages
from words import word_list

display = []
end_of_game = False
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1

print(logo)
print(chosen_word)

for i in range(word_length):
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}, try again.")

    for i in range(word_length):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        print(f"Your guess {guess} is incorrect, you have {lives} lives left")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f"Chosen word is {chosen_word}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(f"{''.join(display)}")
    print(stages[lives])
