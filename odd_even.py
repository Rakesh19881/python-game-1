import random

player_choice = input("Choose Odd or Even: ").lower()
player_number = int(input("Pick a number (1-10): "))
computer_number = random.randint(1, 10)
print(f"Computer picked {computer_number}")

total = player_number + computer_number
print(f"Sum is {total}")

if (total % 2 == 0 and player_choice == "even") or \
   (total % 2 != 0 and player_choice == "odd"):
    print("You win!")
else:
    print("You lose!")
