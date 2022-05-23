#life in weeks
#input - age
#output - age in days/weeks/months
#the range has to be until 90years approx

age = input("How old are you now? ")
age_int = int(age)
years_remaining = 90 - age_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {years_remaining} years, {months_remaining} months, {weeks_remaining} weeks, {days_remaining} days remaining.")