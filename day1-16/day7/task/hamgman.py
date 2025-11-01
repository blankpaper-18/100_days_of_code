import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
# print(chosen_word)
placeholder = ""
for position in range(len(chosen_word)):
    placeholder += "_"
print(placeholder) 
guess =input("guess a letter :").lower()

display = ""

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)

while lives > 0:
    guess =input("guess a letter :").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display = display[:position] + letter + display[position + 1:]
    print(display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        print(stages[lives])
    if "_" not in display:
        print("You win!")
        break
    if lives == 0:
        print("You lose.")
        print(f"The word was {chosen_word}.")
