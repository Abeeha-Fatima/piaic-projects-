import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    your_score : int = 0
    for i in range(NUM_ROUNDS):
        print("round", i + 1)
        computer_num: int = random.randint(1,100)
        your_num: int  = random.randint(1,100)
        print("your number is : ", your_num)
        user_answer:str = input("what do you think  your number is higher or lower? ")
        higher_and_correct : bool = "higher" and computer_num < your_num
        lower_and_correct : bool = "lower" and computer_num > your_num
        if higher_and_correct or lower_and_correct: 
            print("your answer is correct! ", computer_num)
            your_score += 1
        else:
            print("that was incorrect! " , computer_num)
            
    print("now your score is : ", your_score)  
if __name__ == "__main__":
    main()