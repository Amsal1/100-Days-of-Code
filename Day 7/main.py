#Step 3

import random
import hangman_art
import hangman_words

end_of_game = False

chosen_word = random.choice(hangman_words.word_list)

lives = 6

print(hangman_art.logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(0,len(chosen_word)):
    display += '_'



while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print("You already entered this letter, enter any other letter")
        continue

    #Check guessed letter
    flag=0
    for element in range(0,len(chosen_word)):
        if chosen_word[element] == guess:
            display[element] = guess
            flag=1
    if(flag==0):
            lives=lives-1
    if lives == 0:
        print("You lose.")
        end_of_game = True
    
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        print("You won!")
        end_of_game = True
    

    print(hangman_art.stages[lives])
    
    
    
    