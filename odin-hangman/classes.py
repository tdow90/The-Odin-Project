import random
import pickle

class Hangman:
    
    def __init__(self, p1name):
        self.p1name = p1name
        self.num_of_guesses = 0
        with open('google-10000-english-no-swears.txt', 'r') as f:
            data = f.readlines()
        self.word = data[random.randint(0, len(data))]
        self.hidden_word = ''
        for i in range(len(self.word)-1):
            self.hidden_word += '_'

    def make_guess(self, letter): #need user input for the letter to guess
        self.indexes_of_match = []
        self.letter = letter
        for index, character in enumerate(self.word):
            if character == self.letter:
                self.indexes_of_match.append(index)
        return(self.indexes_of_match)
    
    def check_guess(self, letter):
        index = Hangman.make_guess(self, letter)
        if self.letter in self.word:
            for i in index:
                self.hidden_word = self.hidden_word[:i] + self.letter + self.hidden_word[i+1:]
        else:
            self.num_of_guesses = self.num_of_guesses + 1
        print(self.hidden_word)


    def play_game(self):
        save_or_play = ''
        while self.num_of_guesses < 7:
            if save_or_play == 'yes':
                with open('game.pickle', 'wb') as f:
                    pickle.dump(Hangman(self), f)
                    exit()
            else:
                if '_' in self.hidden_word:
                    guess = input(f"{self.p1name}, please guess a letter.\n")
                    Hangman.check_guess(self, guess)
                    print(f'{self.p1name}, you have {7-self.num_of_guesses} guesses left.')
                    print(self.hidden_word)
                else:
                    print(f"You win, you guessed the word, congrats {self.p1name}!")
                    exit()
            save_or_play = input('do you want to save(yes/no)')
        print(f"Sorry {self.p1name}, you're out of guesses. Game over!")
      