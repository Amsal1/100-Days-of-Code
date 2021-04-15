# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n1l=name1.lower()
n2l=name2.lower()

count1=n1l.count('t')+n1l.count('r')+n1l.count('u')+n1l.count('e')+n2l.count('t')+n2l.count('r')+n2l.count('u')+n2l.count('e')
count2=n2l.count('l')+n2l.count('o')+n2l.count('v')+n2l.count('e')+n1l.count('l')+n1l.count('o')+n1l.count('v')+n1l.count('e')

love_score=int(str(count1)+str(count2))

if(love_score<10 or love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score<50 and love_score>40):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")