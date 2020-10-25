import random
class card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def showCard(self):
        return str(str(self.value) + " of " + self.suit)

suits = {'Hearts', 'Spades', 'Clubs', 'Diamonds'}
values = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

deck = {}

x = 1
for s in suits:
    for v in values:
        deck[x] = card(v, s)
        x += 1

player = []
dealer = []

givep = True
i = 0

while i < 4:
    rand = random.randrange(0, 53)
    if rand in deck:
        if givep == True:
            player.append(deck[rand])
            #print(rand, "player")
        else:
            dealer.append(deck[rand])
            #print(rand, "dealer")

        givep = not givep
        i += 1
        deck.pop(rand)

def Hit():
    print("You hit")


def Fold():
    print("You folded")

def Move():
    print("Your cards are the" , player[0].value, "of" , player[0].suit , "and the" , player[1].value, "of" , player[1].suit)
    hf = input("Do you want to Hit(h), or Fold(f) ")
    if hf == 'h':
        Hit()
    elif hf == 'f':
        Fold()
    else:
        print("please enter h to hit or f to fold ")
Move()
