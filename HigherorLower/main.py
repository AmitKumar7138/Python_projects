from art import logo
from art import vs
from game_data import data
import random

print(logo)


def display(item1, item2):
  print(
    f"Compare A : {item1['name']},{item1['description']},from {item1['country']}"
  )
  print(vs)
  print(
    f"Compare B : {item2['name']},{item2['description']},from {item2['country']}"
  )

def choice():
  item1 = random.choice(data)
  item2 = random.choice(data)
  while item1 == item2 or int(item1['follower_count']) == int(item2['follower_count']):
    item2 = random.choice(data)
  return item1,item2

def compare(item1, item2):
  if int(item1['follower_count']) > int(item2['follower_count']): 
    return 'A'
  else:
    return 'B'

points = 0

while True:
  item1, item2 = choice()
  display(item1, item2)
  answer = input("Which one has more followers? Type 'A' or 'B': ").upper()
  if answer == compare(item1, item2):
    points += 1
    print("You're right!")
  else:
    print("You're wrong!")
    break

print(f"Your final score is: {points}")


