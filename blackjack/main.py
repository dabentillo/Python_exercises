import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ACE = 11

from art import logo

user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n':")
print(logo)

#deal another card
def deal_card():
  card = random.choice(cards)
  return card

#generate 2 random cards for the user and computer
def get_cards():
  card_list = []
  for deal in range (2):
    card_list.append(deal_card())
  
  return card_list

#add the on hand cards
def calculate_score(cards_onhand):
  #check for a blackjack (a hand with only 2 cards: ace + 10)
  if ((sum(cards_onhand) == 21) and (len(cards_onhand) == 2)):
    return 0

  #If the score is already over 21, remove the 11 and replace it with a 1
  if(((ACE in cards_onhand)) and (sum(cards_onhand) > 21)):
    cards_onhand.remove(ACE)
    cards_onhand.append(1)
  
  return sum(cards_onhand)
  
#compare the user and computer scores
def compare(user_total, computer_total):
    if (user_total == computer_total):
      print("It's a draw!")
    elif (computer_total == 0):
      print("Computer wins with a Blackjack! You Lose!")
    elif (user_total == 0):
      print("You win with a Blackjack!")
    elif (computer_total > 21):
      print("Computer went over. You win!")
    elif (user_total > 21):
      print("You went over. You lose!")
    elif (user_total > computer_total):
      print("You win!")
    elif (computer_total > user_total):
      print("Computer wins!")

is_game_over = False

while not is_game_over:
  #draw 2 cards for the user
  user_cards_onhand = get_cards()
  #draw 2 cards for the computer
  computer_cards_onhand = get_cards()
  
  #calculate the total of the cards for the user and computer
  user_cards_total = calculate_score(user_cards_onhand)
  computer_cards_total = calculate_score(computer_cards_onhand)
  
  if(((user_cards_total) == 0) or (computer_cards_total == 0)):
    print(f"Your final hand: {user_cards_onhand}, final score: {user_cards_total}")
    print(f"Computer's final hand : {computer_cards_onhand}, final score: {computer_cards_total}")
    if (user_cards_total) == 0:
      print("You win with a Blackjack!")
    else:
      print("Computer wins with a Blackjack! You Lose!")
  else:
    print(f"Your cards: {user_cards_onhand}, current score: {user_cards_total}")
    print(f"Computer's first card: {computer_cards_onhand[0]}")
  
    if(is_game_over == False):
      if computer_cards_total < 17:
        computer_cards_onhand.append(deal_card())
        computer_cards_total = calculate_score(computer_cards_onhand)
      
      #check if user wants to draw another card
      user_another_deal = input("Type 'y' to get another card, type 'n' to pass:")
    
      if(user_another_deal == 'y'):
        user_cards_onhand.append(deal_card())
        user_cards_total = calculate_score(user_cards_onhand)
        # print(f"Your cards: {user_cards_onhand}, current score: {user_cards_total}")
      else:
        is_game_over = True
  
      print(f"Your final hand: {user_cards_onhand}, final score: {user_cards_total}")
      print(f"Computer's final hand : {computer_cards_onhand}, final score: {computer_cards_total}")
      compare(user_cards_total, computer_cards_total)

  user_another_game = input("would you like to play another game? Type 'y' or 'n':")
  if (user_another_game == "y"):
    clear()
    is_game_over = False
  else:
    is_game_over = True
    print("Goodbye!")
  
