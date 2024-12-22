import random

#Need to generate a number randomly
num_to_guess = random.randint(0,10) 
print(num_to_guess)

#Need to ask user to guess a number between 0 & 100
guess = int(input('Guess a number between 1 and 100:'))

while guess != num_to_guess:
    if guess > num_to_guess:
        print("To high, guess a smaller numeber")
    elif guess < num_to_guess:
        print("To low, pick a higher number")
    guess = int(input("pick again:"))

print('You win, you guessed right!')
    
    