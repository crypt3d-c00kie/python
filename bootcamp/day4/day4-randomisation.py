#day4
#randomisation and modules
#randint(a,b) creates random whole number between a and b
#random.random() #implies random float number 0-1

import random #module for randint
from my_module import * #importing all values in module my_module

random_integer = random.randint(1,100)
print("Printing the random number from 1-100")
print(random_integer)

print("Printing the pi from custom module")
print(pi1)

#heads or tail randomisation
random_side = random.randint(0,1) #probability space for head and tail is 0 or 1
if random_side == 1:
    print("Heads!")
else:
    print("Tails!!")



