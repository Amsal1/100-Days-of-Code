from art import logo, vs
from data import data
import random

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def check_answer(guess, A, B):
    if(A>B and guess=='a'):
        return True
    elif(B>A and guess=='b'):
        return True
    else:
        return False

print(logo)
score = 0
game_should_continue = True
account_a = get_random_account()
account_b = get_random_account()
while game_should_continue:
    account_a = account_b
    account_b = get_random_account()
    while account_a == account_b:
        account_b = get_random_account()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")