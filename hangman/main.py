import random
import hangmanwords
import hangmanart
from replit import clear

word_display = []
end_of_game = False
num_of_lives = 6

chosen_word = random.choice(hangmanwords.word_list)
word_length = len(chosen_word)

for char in range(0, word_length):
    word_display += "_"

print(hangmanart.logo)

#display the users the number of letters in a word
print(" ".join(word_display))

while not end_of_game:

    letter = input("Guess a letter on the word: ").lower()

    clear()

    if letter.isdigit():  #check if the entered char is a number
        print("number is not allowed. Try again.")
    elif letter in word_display:  #check if the char is already entered previously
        print(f"You've already guessed {letter}")
    elif letter in chosen_word:
        for position in range(0, word_length):
            if letter == chosen_word[position]:
                word_display[position] = letter
    else:
        print(f"{letter} is not on the word. You lose a life.")
        num_of_lives -= 1
        if num_of_lives == 0:
            print("Game Over! You Lose!")
            end_of_game = True

    if not '_' in word_display:
        print("Congratulations! You win!")
        end_of_game = True

    print(hangmanart.stages[num_of_lives])
    print(" ".join(word_display))
