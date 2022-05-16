import random

user_points = 0
computer_points = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit.").lower()
    if user_input == "q":
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors" or user_input == "scissors" and computer_pick == "paper" or user_input == "paper" and computer_pick == "rock":
        user_points += 1
        print()
        print(f"You won!\nYour points: {user_points}, computer's points: {computer_points}.")
        print()
    elif user_input == computer_pick:
        print()
        print(f"Draw.\nYour points: {user_points}, computer's points: {computer_points}.")
        print()
    else:
        computer_points += 1
        print()
        print(f"You lost :(\nYour points: {user_points}, computer's points: {computer_points}.")
        print()

print()   
print(f"Thank you for playing the game! \nYour points: {user_points}, computer's points: {computer_points}.")
