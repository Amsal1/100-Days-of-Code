from art import logo
import os

print(logo)
auction = {}
end = "Yes"
while(end=="Yes" or end=="yes"):
    os.system('cls')
    name = input("Enter your name: ")
    bid_price = int(input("Enter your bid price: "))
    auction[name] = bid_price

    end = input("Are there anyone else who want to bid? Yes or No ")

highest = 0
highest_name = ""
for name in auction:
    if(auction[name]>highest):
        highest_name = name
        highest = auction[name]
print(f"The highest bidder is {highest_name} with a amount of {highest}")