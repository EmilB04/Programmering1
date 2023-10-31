# AUTHOR EMIL BERGLUND #

class Format: # Only for decoration in the terminal
    bold = '\033[1m'
    underline = '\033[4m'
    end = '\033[0m'

''' Functions '''
import random as rd

full_deck = {
    "Two of clubs": 2, "Three of clubs": 3, "Four of clubs": 4, "Five ofclubs": 5, "Six of clubs": 6,
    "Seven of clubs": 7, "Eight of clubs": 8, "Nine of clubs": 9, "Ten of clubs": 10,
    "Jack of clubs": 10, "Queen of clubs": 10, "King of clubs": 10, "Ace of clubs": 11,

    "Two of diamonds": 2, "Three of diamonds": 3, "Four of diamonds": 4, "Five of diamonds": 5,
    "Six of diamonds": 6, "Seven of diamonds": 7, "Eight of diamonds": 8, "Nine of diamonds": 9,
    "Ten of diamonds": 10, "Jack of diamonds": 10, "Queen of diamonds": 10, "King of diamonds": 10,"Ace of diamonds": 11, 

    "Two of hearts": 2, "Three of hearts": 3, "Four of hearts": 4, "Five of hearts": 5, 
    "Six of hearts": 6, "Seven of hearts": 7, "Eight of hearts": 8, "Nine of hearts": 9, "Ten of hearts": 10,
    "Jack of hearts": 10, "Queen of hearts": 10, "King of hearts": 10, "Ace of hearts": 11,

    "Two of spades": 2, "Three of spades": 3, "Four of spades": 4, "Five of spades": 5, "Six of spades": 6,
    "Seven of spades": 7, "Eight of spades": 8, "Nine of spades": 9, "Ten of spades": 10,
    "Jack of spades": 10, "Queen of spades": 10, "King of spades": 10, "Ace of spades": 11,
}

def get_new_shuffled_deck():
    '''
    Create a new shuffled deck of cards
    :return: list
    '''
    deck = list(full_deck.keys())
    rd.shuffle(deck)
    return deck

def get_card_value(card):
    '''
    Get the value of a card
    :param card: string
    :return: int
    '''
    return full_deck[card]

def calculate_hand_value(hand):
    '''
    Calculate the value of a hand
    :param hand: list
    :return: int
    '''
    hand_value = 0

    for card in hand:
        hand_value += get_card_value(card)    # list

    if hand_value > 21: # Check if the hand is larger han 21
        for card in hand:
            # if card is an ace check if it should be 1 or 11 points
            if card == "Ace of clubs" or card == "Ace of diamonds" or card == "Ace of hearts" or card == "Ace of spades":
                hand_value -= 10
                if hand_value <= 21:
                    break
    return hand_value

def fill_hands(player_amount, dealer_amount):
    '''
    Fill the player's hand and remove two cards from the deck
    :param player_amount: int
    :param dealer_amount: int
    '''
    for i in range(player_amount):
        player_hand.append(shuffled_deck.pop())
    for i in range(dealer_amount):
        dealer_hand.append(shuffled_deck.pop())

def check_for_blackjack(hand):
    '''
    Check if the player got blackjack
    If the player got blackjack, the game is over --> natural blackjack
    If the player didn't get blackjack, ask for user choice
    :param hand: list
    :return: string
    :return: function
    '''
    if calculate_hand_value(hand) == 21:
        print("---------------------------------")
        print("-- You got blackjack! You win! --")
        print("---------------------------------\n")
        return "blackjack"
    else:
        return userChoice()

def userChoice():
    '''
    Ask the user if they want to hit or stand
    If the user chooses to hit, they get a new card
    If the user chooses to stand, the dealer plays
    :return: function
    :return: function
    '''
    while True:
        choice = input(f"{Format.underline}Do you want to hit or stand? (h/s):{Format.end} ").lower()
        if choice == "h":
            print("You chose to hit.\n")
            return hit()
        elif choice == "s":
            print("You chose to stand.\n")
            return stand()
        else:
            print("Invalid input. Try again.\n")

def stand():
    '''
    The dealer plays
    :return: string
    '''
    print("The dealer will now play. ")
    while calculate_hand_value(dealer_hand) < calculate_hand_value(player_hand):
        fill_hands(player_amount=0, dealer_amount=1)
    print(f"These are the dealers cards with a total value of {calculate_hand_value(dealer_hand)}: ")
    print_hand(dealer_hand)

    if calculate_hand_value(dealer_hand) > 21:
        print("-------------------------------------")
        print("-- The dealer went bust. You win! --")
        print("-------------------------------------\n")
        return "win"
    elif calculate_hand_value(player_hand) > calculate_hand_value(dealer_hand):
        print("-----------------------------------")
        print("-- You beat the dealer! You win! --")
        print("-----------------------------------\n")
        return "win"
    elif calculate_hand_value(dealer_hand) > calculate_hand_value(player_hand):
        print("-----------------------------------")
        print("-- The dealer beat you! You lose! --")
        print("-----------------------------------\n")
        return "lose"
    elif calculate_hand_value(dealer_hand) == calculate_hand_value(player_hand):
        print("-----------------------------------")
        print("-- You tied with the dealer! --")
        print("-----------------------------------\n")
        return "tie"
    else:
        print("\nSomething went wrong. Please try again.")

def hit():
    '''
    The player gets a new card
    :return: string
    :return: function
    '''
    fill_hands(player_amount=1, dealer_amount=0)
    new_card = player_hand[-1]
    print(f"You have been dealt one new card: '{new_card}'")
    print_hand(player_hand)
    print(f"{Format.bold}The total value of your hand is {calculate_hand_value(player_hand)}.{Format.end}\n ")
    if calculate_hand_value(player_hand) > 21:
        print("-------------------------------------")
        print("-- You went bust. The dealer wins! --")
        print("-------------------------------------\n")
        return "lose"
    elif calculate_hand_value(player_hand) == 21:
        print("---------------------------------")
        print("-- You got blackjack! You win! --")
        print("---------------------------------\n")
        return "blackjack"
    else:
        return userChoice()

def retry(player_chips):
    '''
    Ask the user if they want to play again
    :param player_chips: int
    :return: bool
    '''
    while True:
        choice = input(f"{Format.underline}Do you want to play again? (y/n):{Format.end} ").lower()
        if choice == "y":
            if player_chips == 0:
                print("You don't have any chips left. Better luck next time!")
                return False
            else:
                return True
        elif choice == "n":
            return False
        else:
            print("\nInvalid input. Try again.")

def print_hand(hand):
    '''
    Print the cards in the hand
    :param hand: list
    '''
    for card in hand:
        print(f"- {card}")

# Create a variable for the player's chips
# Needs to be oustide of the loop to not reset every time
player_chips = 5

def input_check_chips(player_chips):
    '''
    Ask the user how many chips they want to bet
    :param player_chips: int
    :return: int
    '''
    while True:
        try:
            bet = int(input(f"\n{Format.underline}You currently have {player_chips} chip(s). How many do you want to bet?{Format.end} "))
            if bet <= 0:
                print("You have to bet at least one chip.")
            elif bet > player_chips:
                print("You don't have that many chips.")
            else:
                print(f"You bet {bet} chips out of {player_chips}.")
                return bet
        except ValueError:
            print("Invalid input. Try again.")

def update_chips(player_chips, bet, result):
    '''
    Update the player's chips according to the result
    :param player_chips: int
    :param bet: int
    :param result: string
    :return: int
    '''
    if result == "blackjack":
        return player_chips + (bet * 2)
    elif result == "win":
        return player_chips + bet
    elif result == "lose":
        return player_chips - bet
    else:          # tie
        return player_chips

''' Main'''

game = True
while game:
    # Create a deck of cards
    shuffled_deck = get_new_shuffled_deck()

    # Create a hand for the player and the dealer
    player_hand = []; dealer_hand = []

    # Fill the hands
    fill_hands(player_amount=2, dealer_amount=2)

    # Ask the user how many chips they want to bet
    bet = input_check_chips(player_chips)

    # Print the hands
    print(f"\nThe cards have been dealt. These are your cards, with a total value of {calculate_hand_value(player_hand)}: ")
    print_hand(player_hand)
    print(f"The dealer's visible card is '{dealer_hand[0]}', with a value of {get_card_value(dealer_hand[0])}.\n")

    # Check for blackjack. 
    #   If blackjack, the game is over --> natural blackjack
    #   If not blackjack, ask for user input

    # User input
    # If the user chooses to hit, they get a new card
    # If the user chooses to stand, the dealer plays
    
    result = check_for_blackjack(player_hand)
    
    # Determine the winner and update the chips accordingly
    player_chips = update_chips(player_chips, bet, result)

    # Ask the user if they want to play again
    game = retry(player_chips)

print("\nThanks for playing!")