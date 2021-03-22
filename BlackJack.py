# BlackJack Game
# Coded by Brian Mariner

import random
# Card class


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self):
        print("{} of {}".format(self.val, self.suit))


# Deck class that contains methods to initialize,shuffle, and deal cards.
class Deck:
    def __init__(self):
        # Initialize cards from hearts, spades, clubs, and diamonds from 1 - 11 and shuffle the deck
        self.cards = []
        self.shuffleDeck()

    def shuffleDeck(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in range(1, 14):
                self.cards.append(Card(s, v))

        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()

    # Deal hand to players/dealer
    def deal(self, playerOne, dealer)
    for i in range(3):

        # draw a card from the top of the deck for a player or dealer

        # Player class that contains methods for what actions a player can do and to evaluate your hand


class Player:
    def __init__(self):
        # flag to declare CPU as a dealer
        isDealer = False
        # draw a card from the deck

        # evaluate the hand to see if what the current score of your hand is
        pass


playGame = True

# Continue playing the game as long as the user wants to play
# while playGame == True:

deck = Deck()
deck.show()
