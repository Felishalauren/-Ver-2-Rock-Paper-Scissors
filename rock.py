import random

choices = ["rock","paper","scissors"]
player_wins = 0
computer_wins = 0
playing = True

while playing: 
    print("Let's play rock, paper or scissors!")
    player = None
    computer = random.choice(choices)

    while player not in choices :
        player = input("\nChoose rock, paper, scissors : ").lower()
    print(f"Player : {player}")
    print(f"Computer : {computer}")


    if (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper") :
        winner = "Player"
    elif player == computer :
        winner = "Tie"
    else :
        winner = "Computer"

    if winner == "Player" :
        player_wins +=1
        print("You Won!")
    elif winner == "Computer" :
        computer_wins +=1
        print("Computer Won!")
    else :
        print("It's a tie!")
    print(f"Current Score : Player - {player_wins} : Computer - {computer_wins}")
    if player_wins > computer_wins :
        print("Congratulations! You Won!")
    elif computer_wins > player_wins :
        print("Computer Won!")

    play_again = input("Play Again ? (y/n) : ").lower()
    if not play_again == "y" :
        playing = False
        print("Thanks for playing! :D")




