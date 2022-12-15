# leap year? perhaps

def isLeap(year):
    """Returns True if the given year is Leap else returns false"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def daysinMonth(year, month):
    """This is a docstring"""
    if month > 12 or month < 1:
        return "Invalid Month"

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(year) and month == 2:
        return 29
    else:
        return month_days[month-1]

def main():
    """The Infamous Main function"""
    year = int(input('Year :: '))
    month = int(input('Month :: '))
    days = daysinMonth(year,month)
    print(f'Days :: {days}')

if __name__ == '__main__':
    main()