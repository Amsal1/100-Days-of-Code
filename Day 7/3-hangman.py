#Step 3

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in len(chosen_word):
    display += '_'

end_of_game = False

while not end_of_game:


    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for element in range(0,len(chosen_word)):
        if chosen_word[element] == guess:
            print("Right")
            display[element] = guess
        else:
            print("Wrong")
    print(display)

    if "_" not in display:
        end_of_game = True