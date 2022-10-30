#day8
#check a number if its prime
#prime number can only divided by itself and 1
def prime_check(val):
    isPrime = True
    for i in range(2,val):
        if val  %i == 0:
            isPrime = False
    if isPrime:
        print("It's a prime number")
    else:
        print("non-prime number")

n = int(input("Enter the number to check if prime : "))
prime_check(n)
