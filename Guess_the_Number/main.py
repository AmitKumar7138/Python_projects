#Number Guessing Game Objectives:
from art import logo
import random
# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

print(logo)
print("Welcome to the Number guessing Game!")
print("I am thinking of a number between 1 and 100.")
diff = input("Choose a difficulty: Type 'easy' or 'hard': ").lower()

# Function to get number of turns from users response
def turns():
  if diff == 'easy':
    n_turns = 10
  elif diff == 'hard':
    n_turns = 5
  else:
    print("Please choose a valid difficulty.")
  return n_turns

# # Function to give hints to the user
def guess(res,num,n_turns):
  if res==num:
    print(f"You got it! The number is: {num}")
    game_over = True
  elif res < num:
    print("Too low. Guess again.")
    print("Guess Again")
    print(f"You have {n_turns-1} guesses left.")
    game_over = False
  else :
    print("Too high. Guess again.")
    print("Guess Again")
    print(f"You have {n_turns-1} guesses left.")
    game_over = False

  return game_over
    
n_turns = turns() # Calling turns function to get number of tuns
num  = random.randint(1,100) # Generates a random integer between 1 and 100
while n_turns > 0: # Loop until number of turns reaches 0 
  res = int(input("Make a guess: "))
  game_over = guess(res,num,n_turns)
  if game_over:
    break
  n_turns -= 1

if n_turns == 0:
  print("You ran out of turns.")
  print("The number was: ",num)

  
  
  