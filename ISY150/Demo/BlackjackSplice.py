MAX = 21


def main():
    hand1 = 0

    hand2 = 0

    deck = create_deck()

    while hand1 <= MAX and hand2 <= MAX:
        card1, value1 = deck.popitem()

        hand1 = update_hand_value(hand1, value1, card1)

        card2, value2 = deck.popitem()

        hand2 = update_hand_value(hand2, value2, card2)

        print('Player 1 was dealt', card1)

        print('Player 2 was dealt', card2)

        print()

    if hand1 > MAX and hand2 > MAX:

        print("There is no winner.")

    elif hand1 > 21:

        print("Player 2 wins.")

    else:

        print("Player 1 wins.")


def create_deck():
    suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

    special_values = {'Ace': 1, 'King': 10, 'Queen': 10, 'Jack': 10}

    numbers = ['Ace', 'King', 'Queen', 'Jack']

    for i in range(2, 11):
        numbers.append(str(i))

    deck = {}

    for suit in suits:

        for num in numbers:

            if num.isnumeric():
                deck[num + ' of ' + suit] = int(num)

    return deck


def update_hand_value(hand, value, card):
    if not card.startswith('Ace'):

        return hand + value

    elif hand > 10:

        return hand + value

    else:

        return hand + 11


main()
