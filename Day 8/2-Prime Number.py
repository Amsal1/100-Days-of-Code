#Write your code below this line 👇

def prime_checker(number):
    num=number-1
    flag=0
    while(num!=1):
        if(number%num==0):
            flag=1
        num-=1
    if(flag==1):
        print("Its not a prime number")
    else:
        print("Its a prime number")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)

