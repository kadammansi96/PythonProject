import random
from art import logo, vs
from game_data import data
from replit import clear

def format_data(account):
  """Takes the account data and returns into printable format"""
  account_name = account["name"]
  account_desc = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_desc}, from {account_country}"

def check_answer(guess, a_follower, b_follower):
  """Takes the user guess and follower counts and returns if they got it right"""
  if a_follower > b_follower:
    return guess == "a"
  else:
    return guess == "b"
    
# Display art
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make the game repeatable
while game_should_continue:
  # Generate the random account from game data

  # Making the position B at A and new at B

  account_a = account_b
  account_b = random.choice(data)
  if account_a == account_b:
    account_b = random.choice(data)
    
  print(f"Compare A : {format_data(account_a)}")
  print(vs)
  print(f"Against B : {format_data(account_b)}\n")
  
  #  Ask the user to guess
  guess = input("Who has most followers. Type 'A' or 'B' : ").lower()
  
  # Check if user is correct
  
  # Get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  is_correct = check_answer(guess, a_follower_count, b_follower_count)

  
  # Give user feedback on their guess and Score keeping
  if is_correct:
    score += 1
    print(f"You're right. Current score : {score}\n")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score : {score}")
  
  
  