print('''    8
           .d8b.
       _.d8888888b._
     .88888888888888b.
    d88888888888888888b
    8888888888888888888
    Y88888888888888888P
   'Y8888888888888P'
  _..._ 'Y88888P' _..._
 .d88888b. Y888P .d88888b.
d888888888b 888 d88888888b
888P  `Y8888888888P'  Y888
 b8b    Y88888888P    d8Y
  `"'  #############  '"`
         dP d8b Yb
     Ob=dP d888b Yb=dO
      `"` O88888O `"`
   jgs     'Y8P'
''')

print("Welcome to the Island")
print("You have been assigned a task to find the ancient treasure.")
choice1 = input("You are at the crossroads, where do you wanna turn? left or right? :: ").lower()
#the above line will convert the input string into the lower case

if choice1 == "left":
  print('You came across a lake that is dark blue, it looks deep but sometimes you never know until you try :: ')
  choice2 = input("Pick one of these options:: swim or wait :: ").lower()
  if choice2 == "wait":
    choice3 = input("Suddenly the mysterious lake dried up by itself and paved way to what something that seems like an ancient treasure box, Do you wanna open it? :: Yes or No :: ").lower()
    if choice3 == "yes":
      print("CONGRATULATIONS, YOU HAVE FOUND THE ANCIENT TREASURE!!")
    else:
      print("You have missed the oppurtunity. GAME OVER.")
  else:
      print("You have been made the shark's brunch!! GAME OVER")

else:
    print("You fell into the Lava Pit. GAME OVER")





