# given dictionary of months and days
# find months with 31 days

def main():
    months = {"Jan" : 31, "Feb" : 28, "Mar" : 31, "Apr" : 30, "May" : 31, "Jun" : 30, "Jul" : 31, "Aug" : 31, "Sep" : 30, "Oct" : 31, "Nov" : 30, "Dec" : 31}
    month_list = []

    key = int(input("Days :: "))
    for days in months:
        if months[days] == key:
            month_list.append(days)
    
    if not month_list:
        print("None found")
    else:
        print(month_list)
    
main()