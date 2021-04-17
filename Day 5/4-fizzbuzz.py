for num in range(1,101):
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
        continue
    elif(num%3==0):
        print("Fizz")
        continue
    elif(num%5==0):
        print("Buzz")
        continue
    else:
        print(num)