#day3
#pizza prices w/ addons such as cheese burst 
#along with different sizes

print("Welcome to Pizza Delivery!")
size = input("Which size pizza do you want? S, M, or L :: ")
add_pepperoni = input("Do you want to add Pepperoni? Y or N :: ")
extra_cheese = input("Would you like extra cheese in it? Y or N :: ")
bill = 0
if size == 'S':
    bill += 15
elif size =='M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

#output
print(f"Your final bill is ${bill}\n")