# basic calculator app
import os
# bundled up basic arithmetic functions
def add(num1, num2):
    """adds two numbers"""
    return num1+num2
def subtract(num1, num2):
    """subtracts num2 from num1"""
    return num1-num2
def multiply(num1, num2):
    """multiplies num1 and num2"""
    return num1*num2
def divide(num1, num2):
    """divides num1 with num2"""
    return num1/num2

def main():
    num1 = float(input('First Number :: '))
    operations = {
        '+' : add,
        '-' : subtract,
        '*' : multiply,
        '/' : divide
    }
    
    shouldContinue = True
    while shouldContinue:
        choice = input('Pick an Operation (+ - * /) :: ')
        if choice not in operations:
            print("Error : Invalid choice")
            return 0
        else:
            num2 = float(input('Next Number :: '))
            result = operations[choice](num1, num2)
            print(f"{num1} {choice} {num2} = {result}")
        
        if input(f"Type 'y' to continue or 'n' to finish :: ") == 'y':
            num1 = result
        else:
            shouldContinue = False
            os.system('cls')
            print(f"Final Answer is {result}")

if __name__ == '__main__':
    main()