import art
import random
from game_data import data
from replit import clear
print(art.logo)

#i want to have a random celeberity chosen and have them be printed as a or b
def vs_game():
  game_over = True
  def random_celeb():
    """Searches through the data and picks a random number from the list"""
    random_number = random.randrange(len(data))
    return random_number
  
    
  
  def compare(A,B):
    """Grabs the two arguements and compares them and returns which ever is higher.If nothing is higher or lower ends the game."""
    if A > B:
      return "A"
    elif B > A:
      return "B"
    else:
      game_over = False
      print("Invalid.")
      return game_over
  
  points = 0
  while game_over:
    
    A = random_celeb()
    B = random_celeb()
    print(f"Your Current points are: {points}")
    print(f"Compare A: {data[A]['name']} ,{data[A]['description']} from {data[A]['country']} ")
    print(art.vs)
    print(f"Compare B: {data[B]['name']} ,{data[B]['description']} from {data[B]['country']}")
    answer = input("Who has more followers: A or B? ").upper()
    
    if answer == compare(data[A]['follower_count'],data[B]['follower_count']):
      clear()
      print (f"You win {data[A]['name']} has a Follower count of {data[A]['follower_count']} and {data[B]['name']} has a count of {data[B]['follower_count']}")
      points += 1
    else:
      game_over = False
      clear()
      print(f"You lose {data[A]['name']} has a Follower count of {data[A]['follower_count']} and {data[B]['name']} has a count of {data[B]['follower_count']}")
      print(f"You had {points} points.")
      
      
      
  
  if game_over == False:
   continu = input("Do you want to play again press Y or N: ").upper()
   if continu == "Y":
     clear()
     vs_game()
      
   else:
    game_over = False
vs_game() 
