# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

left = 90 - int(age)

days = left*365
weeks = left*52
months = left*12

print("You have "+ str(days) +" days, "+ str(weeks) +" weeks, and "+ str(months) +" months left.")