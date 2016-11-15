# This program uses a dictionary as a deck of cards.
def main():
    # Create a deck of cards.
    deck = create_deck()

    # Deal the cards.
    deal_cards(deck)


# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades': 1, '2 of Spades': 2, '3 of Spades': 3,
            '4 of Spades': 4, '5 of Spades': 5, '6 of Spades': 6,
            '7 of Spades': 7, '8 of Spades': 8, '9 of Spades': 9,
            '10 of Spades': 10, 'Jack of Spades': 10,
            'Queen of Spades': 10, 'King of Spades': 10,

            'Ace of Hearts': 1, '2 of Hearts': 2, '3 of Hearts': 3,
            '4 of Hearts': 4, '5 of Hearts': 5, '6 of Hearts': 6,
            '7 of Hearts': 7, '8 of Hearts': 8, '9 of Hearts': 9,
            '10 of Hearts': 10, 'Jack of Hearts': 10,
            'Queen of Hearts': 10, 'King of Hearts': 10,

            'Ace of Clubs': 1, '2 of Clubs': 2, '3 of Clubs': 3,
            '4 of Clubs': 4, '5 of Clubs': 5, '6 of Clubs': 6,
            '7 of Clubs': 7, '8 of Clubs': 8, '9 of Clubs': 9,
            '10 of Clubs': 10, 'Jack of Clubs': 10,
            'Queen of Clubs': 10, 'King of Clubs': 10,

            'Ace of Diamonds': 1, '2 of Diamonds': 2, '3 of Diamonds': 3,
            '4 of Diamonds': 4, '5 of Diamonds': 5, '6 of Diamonds': 6,
            '7 of Diamonds': 7, '8 of Diamonds': 8, '9 of Diamonds': 9,
            '10 of Diamonds': 10, 'Jack of Diamonds': 10,
            'Queen of Diamonds': 10, 'King of Diamonds': 10}

    # Return the deck.
    return deck


# The deal_cards function deals a specified number of cards
# from the deck.
def deal_cards(deck):
    # loop variable
    play_again = 'y'

    # initialize variable
    hand_value1 = 0
    hand_value2 = 0

    # loop through deck until user exit's
    while play_again == 'y':

        # player one hand
        card1, value1 = deck.popitem()
        print('Player one:', card1)
        # if player one's card value is ace (equals 1) and less than 11, ace = 11
        if value1 == 1 and hand_value1 < 11:
            hand_value1 += 11
        # if card total is 11 or greater ace is 1
        elif hand_value1 == 11 and value1 == 1:
            hand_value1 += 1
        # calculate normally
        else:
            hand_value1 += value1

        # player two hand
        card2, value2 = deck.popitem()
        print('Player two:', card2, '\n')
        # if player two's card value is ace (equals 1) and less than 11, ace = 11
        if value2 == 1 and hand_value2 < 11:
            hand_value2 += 11
        # if card total is 11 or greater ace is 1
        elif hand_value2 == 11 and value2 == 1:
            hand_value2 += 1
        # calculate normally
        else:
            hand_value2 += value2

        # determine totals and winners for Blackjack
        if hand_value2 > 21 and hand_value1 > 21:
            print('\nBoth players lose', '\nPlayer one hand:', hand_value1, '\nPlayer two hand:', hand_value2, '\n')
            hand_value1 = 0
            hand_value2 = 0
            play_again = input('Play again? y or n').lower()
        elif hand_value1 > 21:
            print('\nPlayer two wins! \nPlayer one hand:', hand_value1, '\nPlayer two hand:', hand_value2, '\n')
            hand_value1 = 0
            hand_value2 = 0
            play_again = input('Play again? y or n').lower()
        elif hand_value2 > 21:
            print('\nPlayer one wins! \nPlayer one hand:', hand_value1, '\nPlayer two hand:', hand_value2, '\n')
            hand_value1 = 0
            hand_value2 = 0
            play_again = input('Play again? y or n\n').lower()


# Call the main function.
main()
