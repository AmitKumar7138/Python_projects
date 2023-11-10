from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
res = 'yes'
bids = {}
while res=='yes':
  print(logo)
  print("Welcome to the secret auction program.")
  name = input("What is your name?: ").strip()
  bid = int(input("What is your bid?: $"))
  res = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
  bids[name]=bid
  clear()
else:
  print(f"The winner is {max(bids,key=bids.get)} with a bid of ${max(bids.values())}")