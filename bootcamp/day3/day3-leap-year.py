#day 3
#leap year calculation

# on every year that is evenly divisble by 4
# except every year that is evenly divisble by 100
# unless the year is also divisble by 400

print("\nThe leap year calculator")
year = int(input("Year : "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year\n")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year\n")
