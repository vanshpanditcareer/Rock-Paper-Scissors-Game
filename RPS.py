import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move (Rock, Paper, or Scissor): ").capitalize()
computer_choice = random.choice(item_list)

print(f"Your choice: {user_choice}, Computer choice: {computer_choice}")

if user_choice not in item_list:
    print("Invalid choice! Please choose Rock, Paper, or Scissor.")
elif user_choice == computer_choice:
    print("Match Tie!")
elif user_choice == "Rock":
    if computer_choice == "Paper":
        print("Computer Wins!")
    else:
        print("You Win!")
elif user_choice == "Paper":
    if computer_choice == "Scissor":
        print("Computer Wins!")
    else:
        print("You Win!")
elif user_choice == "Scissor":
    if computer_choice == "Rock":
        print("Computer Wins!")
    else:
        print("You Win!")
