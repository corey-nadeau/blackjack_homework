import random
ranks = ('1','2','3','4','5','6','7','8','9','10','11','12','13')
suits = ("Hearts","Clubs","Spades","Diamonds")
values = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "11": 11,
    "12": 12,
    "13": 13,
}
playing=True


class Card():
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    def deal(self):
        one_card = self.deck.pop()
        return one_card
    def shuffle(self):
        random.shuffle(self.deck)


class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]



def hit_or_stay(deck,hand):
    global playing
    while True:
        x = input("\nWould you like to 'hit', or 'stand'? ")
        if x.lower() == "hit":
            hit(deck,hand)
        elif x.lower() == "stand":
            print("Player standing. Dealers turn ")
            playing = False
        else:
            print('You must enter "hit" or "stand": ')
            continue
        break

def hit(deck,hand):
    hand.add_card(deck.deal())

def inPlay(player,dealer):
    print("\nPlayers hand: ", *player.cards, sep="\n ")
    print("\nDealers hand: ")
    print(" ==card hidden== ")
    print('', dealer.cards[1])

def endGame(player,dealer):
    print("\nPlayers hand: ", *player.cards, sep="\n ")
    print("Players hand = ", player.value)
    print("Dealers hand: ",*dealer.cards, sep='\n ')
    print("Dealers hand = ", dealer.value)

def pBust(player,dealer):
    print("\nYou have busted! ")
def dBust(player,dealer):
    print("\nDealer busted, you Won! ")
def pWins(player,dealer):
    print("\nYou Won! ")
def dWins(player,dealer):
    print("\nDealer wins! ")
def tie(player,dealer):
    print("\nIts a Tie game ")

# GAME TIME

while True:
    deck = Deck()
    deck.shuffle()

    p_hand = Hand()
    p_hand.add_card(deck.deal())
    p_hand.add_card(deck.deal())

    d_hand = Hand()
    d_hand.add_card(deck.deal())
    d_hand.add_card(deck.deal())

    inPlay(p_hand, d_hand)

    while playing:
        hit_or_stay(deck,p_hand)
        inPlay(p_hand,d_hand)
        if p_hand.value > 21:
            pBust(p_hand,d_hand)
            break
    if p_hand.value <= 21:
        while d_hand.value < 17:
            hit(deck,d_hand)

        print('\n GAME OVER. HERE ARE THE RESULTS: ')
        endGame(p_hand,d_hand)
        if d_hand.value > 21:
            dBust(p_hand,d_hand)
        elif d_hand.value > p_hand.value:
            dWins(p_hand,d_hand)
        elif d_hand.value < p_hand.value:
            pWins(p_hand,d_hand)
        else:
            tie(p_hand,d_hand)

    newGame = input('Play again? "yes" or "no": ')
    if newGame.lower() == 'yes':
        playing = True
    else:
        print('\nThanks for coming! \n')
        break
