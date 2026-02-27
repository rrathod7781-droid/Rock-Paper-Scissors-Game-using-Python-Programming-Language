#Building my first game in python by my self 
import random as r

def game_main():
    list1 = ["rock", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = r.choice(list1)
        print(f"Computer's choice is : {computer_choice}")
        if (user_choice == computer_choice):
            print("It's a tie!")
            return 0
        elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
            print("Congratulations! You win!😊💕")
            return 1
        else:
            print("It Sad 😭 You lose!")
            return -1             

user_choice = 0
computer_choice = 0

n = int(input("Enter How many rounds you want to play : "))

for i in range(1,n+1):
    print(f"Round {i} :")
    result = game_main()

    if (result == 1):
        user_choice += 1
    elif (result == -1):
        computer_choice += 1

if (user_choice == computer_choice):
    print(f"\nIt's a tie overall!👍 \nScore of Computer is : {computer_choice} \nYour Score is : {user_choice}")
elif (user_choice > computer_choice):
    print(f"\nCongratulations! You win overall!😊💕\nScore of Computer is : {computer_choice} \nYour Score is : {user_choice}")
else:
    print(f"\nComputer wins overall! 😭\nScore of Computer is : {computer_choice} \nYour Score is : {user_choice}")