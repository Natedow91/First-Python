import random

roll = random.randint(1,6)

guess = int(input('Guess the dice roll:\n'))

if guess == roll:
    print("Nailed it - computer rolled a " + str(roll))
else: 
    print("Nope, computer rolled a " + str(roll))