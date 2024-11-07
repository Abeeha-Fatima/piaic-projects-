# to add two numbers from the user and display thier result
def main ():
    print ("this program add's two numbers")
    num1: str =input ("enter your first number") # ke input in string the converted into int
    num1: int = int(num1)
    num2: str=input("enter your second number")
    num2:int=int(num2)
    total:int=num1+num2
    print ("the sum of the two numbers you provided is: " +str(total) )
if __name__ == '__main__':
    main()