from random import randint
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1, 50)
# print(number)
def easy():
  attempts = 10
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high.")
      attempts -= 1
    elif guess < number:
      print("Too low.")
      attempts -= 1
    else:
      print(f"You got it! The answer was {number}.")
      attempts = 0

def hard():
  attempts = 5
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > number:
      print("Too high.")
      attempts -= 1
    elif guess < number:
      print("Too low.")
      attempts -= 1
    elif guess == number:
      print(f"You got it! The answer was {number}.")
      attempts = 0
    else:
      print("You've run out of guesses, you lose.")
      
if level == "easy":
  easy()
else:
  hard()