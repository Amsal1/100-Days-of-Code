from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game")
print("I am thinking of a number between 1 to 100")
num = random.randint(1,100)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
attempts=10
if(difficulty=='hard'):
  attempts=5
guess = 0
while(attempts!=0):
  guess = int(input("Make a guess: "))
  if(guess>num):
    print("Too high")
  elif(guess<num):
    print("Too low")
  elif(guess==num):
    print(f"You got it! The answer is {num}")
    break
  print("Guess again")
  attempts-=1
  print(f"You have {attempts} attempts remaining to guess the number")

  

