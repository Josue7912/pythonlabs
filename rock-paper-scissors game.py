import random
user = input("Enter your choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)
print(f"You choose {user}, computer choose {computer}")
if user == "computer":
    print("It's a tie")
elif user == "rock":
    if computer == "scissors":
        print("User wins!")
    else:
        print("Computer wins! Paper covers Rock")
elif user == "paper":
    if computer == "rock":
        print("User Wins!")
    else:
        print("Computer Wins! Scissors cut Paper")
elif user == "scissors":
    if computer == "paper":
        print("Users Wins!")
    else:
        print("Computer Wins! Rock smashes Scissors")

