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

import random
game_images = [rock,paper,scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
print(game_images[user])

computer=random.randint(0,2)

print("Computer choose:")
print(game_images[computer])

if(user==0 and computer==0):
    print("Its a draw")
elif(user==0 and computer==1):
    print("You lose")
elif(user==0 and computer==2):
    print("You won")

elif(user==1 and computer==0):
    print("You won")
elif(user==1 and computer==1):
    print("Its a draw")
elif(user==1 and computer==2):
    print("You lose")

elif(user==2 and computer==0):
    print("You lose")
elif(user==2 and computer==1):
    print("You won")
elif(user==2 and computer==2):
    print("Its a draw")