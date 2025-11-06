data = input("Welcome to this unit conversion system. What do you want to convert today 'C2F or F2C' or 'M2F or F2M")
number = float(input("Insert the value that you want to convert"))


def unit_conversion(data, number):
    if data == "C2F":
        result = (number * 9/5) + 32
        print(f"The converted value is {result} Degree Fahrenheit")
    elif data == "F2C":
        result = (number - 32) * 5/9
        print(f"The converted value is {result} Degree Celsius")
    elif data == "M2F":
        result = (number * 3.28084)
        print(f"The converted value is {result} Feet")
    elif data == "F2M":
        result = (number * 0.3048)
        print(f"The converted value is {result} Meters")
    else:
        print("Your input is invalid.")
        
        
unit_conversion(data, number)
