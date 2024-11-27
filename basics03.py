import random
def main():
    computer_num : int = random.randint(1,100)
    while True :
        user_num = int(input("guess my number"))
        if computer_num > user_num:
            print("your number is too low! ")
        elif computer_num < user_num :
            print("your number is too high! ")
        else : 
            print("you gussed my number! ",computer_num)
            break
     


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()