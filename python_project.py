# #Number guessing project

# import random

# rand_user = random.randint(1, 100)
# attempt = 1



# while True:
#     user_choice = int(input("enter your number: "))
#     attempt +=1
#     if user_choice < rand_user:
#         print("To low! Try Again. Thank you")
#     elif user_choice > rand_user:
#         print("To high! Try Again. Thank you")
#     else:
#         print("You select Correct Number. Oh Nice!")
#         break
# print("You Try This Attempt ", attempt)
# print("====Game Over====")


import random

# Choices
choices = ["rock", "paper", "scissors"]

# Scores dictionary
scores = {"player": 0, "computer": 0}

# Play 5 rounds
for round in range(1, 6):
    print(f"\nRound {round}")
    player_choice = input("Enter rock, paper, or scissors: ").lower()

    # Validate input
    if player_choice not in choices:
        print("Invalid choice, try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win this round!")
        scores["player"] += 1
    else:
        print("Computer wins this round!")
        scores["computer"] += 1

# Final scores
print("\nFinal Scores:")
print(f"You: {scores['player']} | Computer: {scores['computer']}")

if scores["player"] > scores["computer"]:
    print("Congratulations! You won the game!")
elif scores["player"] < scores["computer"]:
    print("Computer won the game! Better luck next time.")
else:
    print("The game is a tie!")


