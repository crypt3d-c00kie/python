# Integers Float - Working with Numeric Data


def main():
    val = 3
    val2 = 2
    print(f"Value :: {val}, Type :: {type(val)}") # type(variable) to find the type of variable 

    '''
    Addition        : 3+2
    Subtraction     : 3-2
    Multiplication  : 3*2
    Division        : 3/2  ;; gives out floating value
    Floor Division  : 3//2 ;; gives out integer value
    Exponent        : (3^2) 3**2
    Modulus         : 3%2 ;; remainder = 2? then even ;; else odd
    '''
    print(f"Val1 is {val}, Val2 is {val2}")
    print(f"Addition        : {val+val2}")
    print(f"Subtraction     : {val-val2}")
    print(f"Multiplication  : {val*val2}")
    print(f"Division        : {val/val2}")
    print(f"Floor Division  : {val//val2}")
    print(f"Exponent        : {val**val2}")
    print(f"Modulus         : {val%val2}")

    neval = -22
    # abs(neval)
    print(f"neval : {neval},  abs() : {abs(neval)}")
    
    floaty = 7.475
    # round(variable_name, round to which digit after decimal) rounds up the value to the nearest higher
    print(f"floaty : {floaty}, round() : {round(floaty)}")
    print(f"rounding to 1 : {round(floaty, 1)}")
    print(f"rounding to 2 : {round(floaty, 2)}")

    print("<> Comparisons <> returns booleans")
    
    '''
    #Comparisons:
    #Equal:            3 == 2
    #Not Equal:        3 != 2
    #Greater Than:     3 > 2
    #Less Than:        3 < 2
    #Greater or Equal: 3 >= 2
    #Less or Equal:    3 <= 2
    '''
    num1 = 3
    num2 = 2
    print(f"Num1 : {num1}, Num2 : {num2}")
    print(f"Equal? : {num1 == num2}")
    print(f"Not Equal? : {num1 != num2}")
    print(f"Greater Than? : {num1 > num2}")
    print(f"Less than? : {num1 < num2}")
    


if __name__ == '__main__':
    main()