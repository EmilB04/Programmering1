# AUTHOR EMIL BERGLUND #

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
    # If the player got blackjack, the game is over
    # If the player didn't get blackjack, ask for user choice
    if bjm.calculate_hand_value(hand) == 21:
        print("---------------------------------")
        print("-- You got blackjack! You win! --")
        print("---------------------------------")
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
            hit()
            return True
        elif choice == "s":
            print("\nYou chose to stand.")
            stand()
            return False
        else:
            print("\nInvalid input. Try again.")

def stand():
    print(f"The dealers cards are '{dealer_hand}', with a value of {bjm.calculate_hand_value(dealer_hand)}")

    if bjm.calculate_hand_value(dealer_hand) > 21:
        print("\n-------------------------------------")
        print("-- The dealer went bust. You win! --")
        print("-------------------------------------\n")
    elif bjm.calculate_hand_value(player_hand) > bjm.calculate_hand_value(dealer_hand):
        print("\n-----------------------------------")
        print("-- You beat the dealer! You win! --")
        print("-----------------------------------\n")
    elif bjm.calculate_hand_value(dealer_hand) > bjm.calculate_hand_value(player_hand):
        print("\n-----------------------------------")
        print("-- The dealer beat you! You lose! --")
        print("-----------------------------------\n")
    elif bjm.calculate_hand_value(dealer_hand) == bjm.calculate_hand_value(player_hand):
        print("\n-----------------------------------")
        print("-- You tied with the dealer! --")
        print("-----------------------------------\n")
    else:
        print("\nSomething went wrong. Please try again.")


def hit():
    fill_hands(player_amount=1, dealer_amount=0)
    print(f"You have {player_hand}, with a total value of {bjm.calculate_hand_value(player_hand)}.")
    if bjm.calculate_hand_value(player_hand) > 21:
        print("\n-------------------------------------")
        print("-- You went bust. The dealer wins! --")
        print("-------------------------------------\n")
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


''' Main'''
game = True
while game:
    # Create a deck of cards
    shuffled_deck = bjm.get_new_shuffled_deck()

    # Create a hand for the player and the dealer
    player_hand = []; dealer_hand = []

    # Fill the hands
    fill_hands(player_amount=2, dealer_amount=2)

    # Print the hands
    print(f"The cards have been dealt. You have '{player_hand[0]}' and '{player_hand[1]}', with a total value of {bjm.calculate_hand_value(player_hand)}.")
    print(f"The dealer's visible card is '{dealer_hand[0]}', with a value of {bjm.get_card_value(dealer_hand[0])}.")

    # Check for blackjack. If not blackjack, ask for user choice
    # If the user chooses to hit, they get a new card
    # If the user chooses to stand, the dealer plays
    check_for_blackjack(player_hand)

    # Ask the user if they want to play again
    game = retry()

print("\nThanks for playing!")