#day 2
#tip calculator
#get bill from user, split with n people with n% tip
#output will be a float with 2 decimals
#algo : bill * tip percentage
# / result by nSplit


print("Welcome to the Tip Calculator.")
bill = float(input("What was the bill? "))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12, 15? "))
nSplit = int(input("How many people to split the bill? "))

tip_percentage = tip_percentage/100

bill_with_tip = tip_percentage * bill + bill
nResult = bill_with_tip/nSplit

print("Therefore each person has to pay : ", round(nResult,2))
