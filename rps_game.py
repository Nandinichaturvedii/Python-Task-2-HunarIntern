import random

option = ('rock', 'paper', 'scissor')
running = True

while running:
    player = None
    computer = random.choice(option)

    while player not in option:
        player = input("Enter your choice (rock, paper, scissor): ").lower()

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("Game tie")
    elif player == 'rock' and computer == 'scissor':
        print("You win")
    elif player == 'paper' and computer == 'rock':
        print("You win")
    elif player == 'scissor' and computer == 'paper':
        print("You win")
    else:
        print("You lose")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print("Thanks for playing!")
