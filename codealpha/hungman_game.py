import random
import hungman_stages  # Make sure you've properly imported hungman_stages
import word_list

chosen_word = random.choice(word_list.words)  # Use word_list.word_list to access the list
lives = 6
#print(chosen_word)

display = ['_' for _ in chosen_word]  # Use chosen_word for length
print(display)
game_over = False
while not game_over:
    print("HINT ::::::::::::)))))))))))")
    print("Things are related to elements of chemistry")
    guessed_letter = input("Guess the letter: ").lower()  # Add parentheses to call lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guessed_letter:
            display[position] = guessed_letter
    print(display)  # Move print statement outside the loop

    if guessed_letter not in chosen_word:
        lives -= 1  # Decrement lives
        if lives == 0:
            game_over = True
            print("YOU LOSE!!")
             # Exit the loop when lives are exhausted

    if '_' not in display:
        game_over = True
        print("You Win")
    print(hungman_stages.stages[lives])  # Correct indentation and add a space before rectify
#Make sure you have a word_list.py file containing the list named word_list and a hungman_stages.py file containing the stages list. Also, ensure that stages is properly defined in hungman_stages.py.





