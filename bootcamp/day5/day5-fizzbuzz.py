#day5
#fizzbuzz problem

#space is 1-100
#if a number is divisible by 3 - fizz
#if a number divisible by 5 - buzz
#if divisible by both - fizzbuzz

for n in range(1,101):
    if(n % 3 == 0 and  n % 5 == 0):
        print("FizzBuzz")
    elif(n % 3 == 0):
        print("Fizz")
    elif(n % 5 == 0):
        print("Buzz")
    else:
        print(n)