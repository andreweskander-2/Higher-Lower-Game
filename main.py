#Import data and packages needed from other sources
import random
from replit import clear
from game_data import data
from art import logo
from art import vs
#Print the user interface with random data

# Variables
user_successes = 0
options = random.sample(data, 2)
option_a = options[0]
option_b = options[1]
prev_selected = options

game_on = True
while game_on:
  #creating a dictionary of the 2 options to enable easier refrencing to them letter by directly linking them to the user input which will be either a or b
  options_dictionaries = {'a': option_a, 'b': option_b}
  #creating a separate dictionary for the follower count for each item in the list to make the comparison easier later in the if statement below
  scores = {'a': option_a['follower_count'], 'b': option_b['follower_count']}
  print(logo)
  print(
    f"\nCompare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}.\n"
  )
  print(vs)
  print(
    f"\nCompare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}.\n"
  )

  #Take user input
  print(f"Your current score is {user_successes}")
  user_input = input(
    "\nWho do you think has more followers? Type 'A' or 'B':").lower()

  #Compare the user input with the right answer
  other_score = ""
  if user_input == "a":
    other_score = "b"
  elif user_input == "b":
    other_score = "a"

  if scores[user_input] > scores[other_score]:
    clear()
    # updating option a to become the option of higher score
    option_a = options_dictionaries[user_input]

    # bringing in a new random option as option b
    currently_selected = [option_a]
    while len(currently_selected) != 2:
      new_option = random.sample(data, 1)
      option_b = new_option[0]
      if option_b not in prev_selected:
        currently_selected.append(option_b)
        prev_selected.append(option_b)
      #print(option_b) -> for testing
    # increase the user score
    user_successes += 1

  #if the user is wrong, print a good luck message with the final score
  else:
    clear()
    print(logo)
    print(
      f"\nSorry, that's wrong. Good Luck Next Time! Final score: {user_successes}. "
    )
    game_on = False
