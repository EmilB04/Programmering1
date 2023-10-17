# AUTHOR EMIL BERGLUND #

import blackjack_module as bjm

''' Functions '''
def fill_hands(player_amount, dealer_amount):
    # Fill the player's hand and remove two cards from the deck
    for i in range(player_amount):
        player_hand.append(shuffled_deck.pop())
    for i in range(dealer_amount):
        dealer_hand.append(shuffled_deck.pop())


''' Main'''
# Create a deck of cards
shuffled_deck = bjm.get_new_shuffled_deck()

# Create a hand for the player and the dealer
player_hand = []; dealer_hand = []

# Fill the hands
fill_hands(player_amount=2, dealer_amount=1)

# Print the hands
print(f"The cards have been dealt. You have '{player_hand[0]}' and '{player_hand[1]}', with a total value of {bjm.calculate_hand_value(player_hand)}.")
print(f"The dealers visible card is '{dealer_hand[0]}', with a value of {bjm.calculate_hand_value(dealer_hand)}.")