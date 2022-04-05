
input_name = input("Hello there, What is your name?\n")
print("Welcome", input_name)

import random

roll = random.randint(1,100)


def guessing():
  guess = int(input('Guess the number:\n'))

  if guess < roll:
      print("Too low guess again")
      guessing()
  elif guess > roll: 
      print("Too high guess again")
      guessing()
  elif guess == roll:
      print("correct well done")
    
guessing()