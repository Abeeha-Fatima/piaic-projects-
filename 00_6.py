#Ask the user for a number and print its square (the product of the number times itself).
def main():
    num1:float=float(input("enter your number: "))
    num2= str (num1*num1)
    print("the square of the number you provided is: "+ num2)
if __name__== '__main__':
    main()
