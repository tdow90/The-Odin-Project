from classes import Hangman
import pickle

save_play = input('Do you want to load save game? (yes or no)')
if save_play == 'yes':
    with open('game.pickle', 'rb') as f:
        game1 = pickle.load(f)
        game1.play_game()
else:
    name = input('Welcome, enter you name to start the game.\n')
    hangman = Hangman(name)
    print(f"Good luck, {hangman.p1name}. You have 7 tries to guess {hangman.hidden_word}.")
    hangman.play_game()