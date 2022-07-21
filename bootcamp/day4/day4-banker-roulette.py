#day4
#banker's roulette
#picks out a random person and that person shall pay for the entire bill

import random #for the random.randint() function
#split string method
#.split(",") will convert the items into a list if separated by comma (,)

name_string = str(input("List the people's name separated by comma : "))
names = name_string.split(",") #puts item into the list
#print(names)


#method1
nItems = len(names)
random_choice = random.randint(0, nItems-1)
print("Method 1 using randomized indexing")
print(f"The person who has to pay today is {names[random_choice]}")

#method2 - with random.choice(x)
print("Method 2 using random.choice() function")
random_person = random.choice(names)
print(f"The person who has to pay today is {random_person}")