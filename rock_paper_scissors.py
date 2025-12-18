import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock Paper Scissors Game")
player = input("Choose rock, paper, or scissors: ").lower()

computer = random.choice(options)
print("Computer chose:", computer)

if player == computer:
    print("It's a tie!")
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("You lose!")
