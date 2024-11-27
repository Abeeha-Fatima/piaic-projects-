def main():
   user_response: str = input("what do you want? ")
   if "joke" in user_response:
       print(" Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'")
   else:
       print("sorry i only respond to joke")
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()