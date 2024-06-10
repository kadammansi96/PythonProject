programming_dictionary = {
  "Bug" : "An error in a program that prevents the program from running as expected." ,
  "Function" : "A piece of code that you can easily call over and over again",
}
print(programming_dictionary["Function"])

# # # Adding new items to dictionary
# programming_dictionary["Loop"] = "The action of doing something over and over again"
# print(programming_dictionary)

# # # Creating an empty dictionary
empty_dictionary = {}

# # # Wipe an existing dictionary
programming_dictionary = {}

# # Loop through a dictionary
for thing in programming_dictionary:
  print(thing) #prints the key
  print(programming_dictionary[thing]) #prints the value of key

# Write a programe to convert scores to grades.

student_scores = {
  "Harry" : 81,
  "Ron" : 78,
  "Hermione" : 99,
  "Draco" : 74,
  "Neville" : 62,
}
student_grades = {}

for student in student_scores:
  score = student_scores[student]
  if score > 90:
    student_grades[student] = "Outstanding"
  elif score > 80:
    student_grades[student] = "Exceeds Expectations"
  elif score > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Fail"

print(student_grades)

# # Nesting

capitals = {
  "France" : "Paris",
  "Germany" : "Berlin",
}

# # Nesting a list in a dictionary

travel_log = {
  "France" : ["Paris", "Lille", "Dijon"],
  "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

# # Nested dictionary in dictionary

travel_log = {
  "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_no_visits" : 12 },
  "Germany" : ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a list

travel_log = [
  {
    "country" : "France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"],     
    "total_no_visits" : 12 
  },
  {
    "country" : "Germany", 
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],     "total_no_visits" : 12
  },
]

# Write a program that adds to a travel_log. You can see add_new_country() function to help you code.

travel_log = [
  {
    "country" : "France", 
    "cities_visited" : ["Paris", "Lille", "Dijon"],     
    "total_no_visits" : 12 
  },
  {
    "country" : "Germany", 
    "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"],     
    "total_no_visits" : 12
  },
]

def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["cities_visited"] = cities_visited
  new_country["total_no_visits"] = times_visited
  travel_log.append(new_country)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

# Write a program to create a secret bidder

from replit import clear
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner =  ""
  for bidders in bidding_record:
    bid_amount = bidding_record[bidders]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidders
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
  if should_continue == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
  