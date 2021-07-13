import random

print("Welcome to R_P_S Game!")
print("""
Choose :
's' for Scissors
'p' for Paper
'r' for Rock
""")

list1 = ['s', 'p', 'r']
computer = random.choice(list1)
player = input('>').lower()

while True:
    if player == 's' and computer == 'r':
        print("You Lose!")
        print(f"Computer choice is : {computer}")
        break

    elif player == 'r' and computer == 's':
        print("You Won!")
        print(f"Computer choice is : {computer}")
        break

    elif player == 'p' and computer == 'r':
        print("You Won!")
        print(f"Computer choice is : {computer}")
        break

    elif player == 'r' and computer == 'p':
        print("You Lose!")
        print(f"Computer choice is : {computer}")
        break

    elif player == 's' and computer == 'p':
        print("You Won!")
        print(f"Computer choice is : {computer}")
        break

    elif player == 'p' and computer == 's':
        print("You Lose!")
        print(f"Computer choice is : {computer}")
        break

    elif player == computer:
        print("It's DRAW!")
        print(f"Computer choice is : {computer}")
        break

    else:
        print("Invalid Input")
        print(f"Computer choice is : {computer}")
        break




