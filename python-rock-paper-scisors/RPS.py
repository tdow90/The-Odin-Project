import random


def computerPlay():
    computerOptions = ['rock', 'paper', 'scissors']
    play = computerOptions[random.randint(0,2)]
    return play

def playGame():
   playerScore = 0
   computerScore = 0
   while playerScore < 3 or computerScore < 3:
        playerMove = input("whats your play? ")
        computerMove = computerPlay()
        print(computerMove)
        if playerMove == 'rock' and computerMove == 'scissors':
            playerScore = playerScore + 1
            print(f"You win, {playerMove} beats {computerMove}!")
            print(f"{playerScore} {computerScore}")
        elif playerMove == 'scissors' and computerMove == 'paper':
            playerScore = playerScore + 1
            print(f"You win, {playerMove} beats {computerMove}!")
            print(f"{playerScore} {computerScore}")
        elif playerMove == 'paper' and computerMove == 'rock':
            playerScore = playerScore + 1
            print(f"You win, {playerMove} beats {computerMove}!")
            print(f"{playerScore} {computerScore}")
        elif computerMove == 'rock' and playerMove == 'scissors':
            computerScore = computerScore + 1
            print(f"You win, {computerMove} beats {playerMove}!")
            print(f"{playerScore} {computerScore}")
        elif computerMove == 'scissors' and playerMove == 'paper':
            computerScore = computerScore + 1
            print(f"You win, {computerMove} beats {playerMove}!")
            print(f"{playerScore} {computerScore}")
        else:
            computerScore = computerScore + 1
            print(f"You win, {computerMove} beats {playerMove}!")
            print(f"{playerScore} {computerScore}")
   print(f"game over: {playerScore} {computerScore}")

        
playGame()

