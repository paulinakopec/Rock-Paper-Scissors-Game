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
    #rock: 0, paper:1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors" or user_input == "scissors" and computer_pick == "paper" or user_input == "paper" and computer_pick == "rock":
        print(f"You won! Computer picked {computer_pick}.")
        user_points += 1
        print(f"Your points: {user_points}, computer's points: {computer_points}.")
    elif user_input == computer_pick:
        print(f"Draw - computer also picked {computer_pick}.")
        print(f"Your points: {user_points}, computer's points: {computer_points}.")
    else:
        print("Oh no! You lost :(")
        print(f"Computer picked {computer_pick}.")
        computer_points += 1
        print(f"Your points: {user_points}, computer's points: {computer_points}.")
   
print(f"Thank you for playing the game! \nYour points: {user_points}, computer's points: {computer_points}.")

