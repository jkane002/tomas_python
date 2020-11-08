import random
class card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def showCard(self):
        return str(str(self.value) + " of " + self.suit)

suits = {'Hearts', 'Spades', 'Clubs', 'Diamonds'}
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

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


def loss():
    print('you lost!')

def Hit():
    print('--------------------------------')
    rand1 = random.randrange(0, 53)
    player.append(deck[rand1])

    print("you pulled a" , player[2].value, "of" , player[2].suit )
    h1 = values.get(player[0].value)
    h2 = values.get(player[1].value)
    h3 = values.get(player[2].value)
    total = h1 + h2 + h3

    print("your total is" , total)
    #print("your have" , CardC , "cards")
    print('--------------------------------')
    Move()
    #deck.pop(rand)
    #print("You got the" , player[0].value, "of" , player[0].suit )


def Stand():
    print("You stood")

def Move():
    print("Your cards are the" , player[0].value, "of" , player[0].suit , "and the" , player[1].value, "of" , player[1].suit)
    m1 = values.get(player[0].value)
    m2 = values.get(player[1].value)
    total = m1 + m2
    print("your total is" , total)
    #print("your have" , CardC , "cards")
    hf = input("Do you want to Hit(h), Stand(s) ")
    if hf == 'h':
        Hit()
    elif hf == 's':
        Stand()
    else:
        print("please enter h to hit, or s to stand ")
Move()

if total > 21:
    loss()
#make 2 player mode against computer
#in list player print list and add together for total
