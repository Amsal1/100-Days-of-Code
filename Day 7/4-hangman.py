#Step 3

import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

end_of_game = False
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for i in range(0,len(chosen_word)):
    display += '_'



while not end_of_game:
    guess = input("Guess a letter: ").lower()

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
    print(stages[lives])
    
    if "_" not in display:
        print("You won")
        end_of_game = True
    
    