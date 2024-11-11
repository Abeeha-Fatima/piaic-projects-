#Write a program which prompts the user for a temperature in Fahrenheit (this can be a number with decimal places!) and outputs the temperature converted to Celsius.
def main():
    temp_in_farenhite:float=float(input("enter temperature in farenhite: "))
    temp_in_degrees:float=(temp_in_farenhite -32)*5.0/9.0
    print("converted to degrees = " + str(temp_in_degrees ))
if __name__ =='__main__':
    main()