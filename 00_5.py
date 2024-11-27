#Prompt the user to enter the lengths of each side of a triangle and then calculate and print the perimeter of the triangle (the sum of all of the side lengths).
def main():
    side_1:float=float(input("enter the length of side 1: "))
    side_2:float=float(input("enter the length of side 2: "))
    side_3:float=float(input("enter the length of side 3: "))
    total=str(side_1+side_2+side_3)
    print("the perimeter of the triangle is: " + total)

if __name__ == '__main__':
    main()