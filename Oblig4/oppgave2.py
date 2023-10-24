# AUTHOR EMIL BERGLUND #

#TODO
# Hvis spilleren er tom for chips, skal spilles avsluttes
# Legg funksjoner i en egen fil

import blackjack_module as bjm

''' Functions '''
def fill_hands(player_amount, dealer_amount):
    # Fill the player's hand and remove two cards from the deck
    for i in range(player_amount):
        player_hand.append(shuffled_deck.pop())
    for i in range(dealer_amount):
        dealer_hand.append(shuffled_deck.pop())

def check_for_blackjack(hand):
    # Check if the player got blackjack
    # If the player got blackjack, the game is over --> natural blackjack
    # If the player didn't get blackjack, ask for user choice
    if bjm.calculate_hand_value(hand) == 21:
        print("---------------------------------")
        print("-- You got blackjack! You win! --")
        print("---------------------------------")
        return "blackjack"
    else:
        return userChoice()

def userChoice():
    # Ask the user if they want to hit or stand
    # If the user chooses to hit, they get a new card
    # If the user chooses to stand, the dealer plays
    while True:
        choice = input("\nDo you want to hit or stand? (h/s): ").lower()
        if choice == "h":
            print("\nYou chose to hit.")
            return hit()
        elif choice == "s":
            print("\nYou chose to stand.")
            return stand()
        else:
            print("\nInvalid input. Try again.")

def stand():
    fill_hands(player_amount=0, dealer_amount=1)
    print(f"These are the dealers cards with a total value of {bjm.calculate_hand_value(dealer_hand)}: ")
    print_hand(dealer_hand)

    if bjm.calculate_hand_value(dealer_hand) > 21:
        print("\n-------------------------------------")
        print("-- The dealer went bust. You win! --")
        print("-------------------------------------\n")
        return "win"
    elif bjm.calculate_hand_value(player_hand) > bjm.calculate_hand_value(dealer_hand):
        print("\n-----------------------------------")
        print("-- You beat the dealer! You win! --")
        print("-----------------------------------\n")
        return "win"
    elif bjm.calculate_hand_value(dealer_hand) > bjm.calculate_hand_value(player_hand):
        print("\n-----------------------------------")
        print("-- The dealer beat you! You lose! --")
        print("-----------------------------------\n")
        return "lose"
    elif bjm.calculate_hand_value(dealer_hand) == bjm.calculate_hand_value(player_hand):
        print("\n-----------------------------------")
        print("-- You tied with the dealer! --")
        print("-----------------------------------\n")
        return "tie"
    else:
        print("\nSomething went wrong. Please try again.")


def hit():
    fill_hands(player_amount=1, dealer_amount=0)
    print(f"These are your cards, with a total value of {bjm.calculate_hand_value(player_hand)}: ")
    print_hand(player_hand)
    if bjm.calculate_hand_value(player_hand) > 21:
        print("\n-------------------------------------")
        print("-- You went bust. The dealer wins! --")
        print("-------------------------------------\n")
        return "lose"
    elif bjm.calculate_hand_value(player_hand) == 21:
        print("\n---------------------------------")
        print("-- You got blackjack! You win! --")
        print("---------------------------------\n")
        return "blackjack"
    else:
        return userChoice()

def retry():
    while True:
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("\nInvalid input. Try again.")

def print_hand(hand):
    for card in hand:
        print(f"- {card}")


def input_check_chips(player_chips):
    if player_chips > 0:
        bet = True
    else:
        bet = False

    while bet:
        try:
            print(f"You have {player_chips} chips.")
            bet = int(input("\nHow many chips do you want to bet? "))
            if bet <= 0:
                print("You have to bet at least one chip.")
            elif bet > player_chips:
                print("You don't have that many chips.")
            else:
                print("You bet", bet, "chips.")
                return bet
        except ValueError:
            print("Invalid input. Try again.")

''' Main'''
player_chips = 5

def update_chips(player_chips, bet, result):
    if result == "blackjack":
        return player_chips + (bet * 2)
    elif result == "win":
        return player_chips + bet
    elif result == "lose":
        return player_chips - bet
    else:
        return player_chips

game = True
while game:
    # Create a deck of cards
    shuffled_deck = bjm.get_new_shuffled_deck()

    # Create a hand for the player and the dealer
    player_hand = []; dealer_hand = []

    # Fill the hands
    fill_hands(player_amount=2, dealer_amount=2)

    # Ask the user how many chips they want to bet out of the predefined amount (5)
    bet = input_check_chips(player_chips)

    # Print the hands
    print(f"\nThe cards have been dealt. These are your cards, with a total value of {bjm.calculate_hand_value(player_hand)}: ")
    print_hand(player_hand)
    print(f"The dealer's visible card is '{dealer_hand[0]}', with a value of {bjm.get_card_value(dealer_hand[0])}.")


    # Check for blackjack. If not blackjack, ask for user choice
    # If the user chooses to hit, they get a new card
    # If the user chooses to stand, the dealer plays
    result = check_for_blackjack(player_hand)

    if result == "blackjack":
        player_chips = update_chips(player_chips, bet, result)
    else:
        # Player's choice
        game_end = True
        if result == "hit":
            result = hit()
        elif result == "stand":
            result = stand()

        # Determine the winner
        player_chips = update_chips(player_chips, bet, result)

    # Ask the user if they want to play again
    game = retry()

print("\nThanks for playing!")