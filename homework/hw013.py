import random

class card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def showCard(self):
        return str(str(self.value) + " of " + self.suit)
#variables
suits = {'Hearts', 'Spades', 'Clubs', 'Diamonds'}
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

deckb = {}
deckw = {}
giveToHand1 = True
hand1 = []
hand2 = []
player = []
dealer = []
givep = True
i = 0
ok = True
x = 1
for s in suits:
    for v in values:
        deckw[x] = card(v, s)
        x += 1

x = 1
for s in suits:
    for v in values:
        deckb[x] = card(v, s)
        x += 1

while i < 4:
    rand = random.randrange(0, 53)
    if rand in deckb:
        if givep == True:
            player.append(deckb[rand])
            #print(rand, "player")
        else:
            dealer.append(deckb[rand])
            #print(rand, "dealer")

        givep = not givep
        i += 1
        deckb.pop(rand)

while len(deckw) > 0:
    rand = random.randrange(0, 53)
    if rand in deckw:
        #print(rand)
        if giveToHand1 == True:
            hand1.append(deckw[rand])
        else:
            hand2.append(deckw[rand])
        #print(len(deck))
        deckw.pop(rand)

        giveToHand1 = not giveToHand1

while i < 4:
    rand = random.randrange(0, 53)
    if rand in deckb:
        if givep == True:
            player.append(deckb[rand])
            #print(rand, "player")
        else:
            dealer.append(deckb[rand])
            #print(rand, "dealer")

        givep = not givep
        i += 1
        deckb.pop(rand)


#blackjack
def Hit():
    print('--------------------------------')
    rand1 = random.randrange(0, 53)
    player.append(deckb[rand1])
    for i in range(0, len(player)):
        if i == (len(player)-1):
            print("You pulled a", player[i].value, "of" , player[i].suit)
    print('--------------------------------')
    Move()

def loss():
    print("You lose!")
    ok = False
    tt = True

def Move():
    print("Your cards are the:")
    for w in range(len(player)):
        print(player[w].value, "of" , player[w].suit)

    hf = input("Do you want to Hit(h), Stand(s) ")
    if hf == 'h':
        Hit()
    elif hf == 's':
        Stand()
    else:
        print("please enter h to hit, or s to stand ")

def Stand():
    dealer = random.randrange(4, 21)
    print('--------------------------------')
    print("your total was" , total)
    print("the dealers total was" , dealer)
    if total > dealer:
        print("You won!")
    elif dealer > total:
        print("You lost!")
    elif total == dealer:
        print("You tied!")
    else:
        print("something weird happened")
    print('--------------------------------')

#war game
def compare():
    #if len(hand1) > len(hand2):
        #losingTeam = len(hand2)
        #else:
        #losingTeam = len(hand1)
    wins1 = 0
    wins2 = 0
    round = 0
    place1 = 0
    place2 = 0
    while len(hand1) > 0 or len(hand2) > 0:
        fighter1 = hand1[place1]
        fighter2 = hand2[place2]
        print('Your card:' , fighter1.value)
        print('Opponents card:' , fighter2.value)
        if fighter1.value > fighter2.value:
            print(fighter1.showCard() , "wins!")
            hand1.append(fighter2)
            hand2.remove(fighter2)
            wins1 += 1
        elif fighter1.value < fighter2.value:
            print(fighter2.showCard() , "wins!")
            hand2.append(fighter1)
            hand1.remove(fighter1)
            wins2 += 1
        else:
            place1 += 1
            place2 += 1



            print("Tie!")
        print('Your score:' , len(hand1))
        print('Opponents score:' , len(hand2))
        print('----------------------------------')
        if place1 < len(hand1)-1:
            place1 += 1
        else:
            place1 = 0

        if place2 < len(hand2)-1:
            place2 += 1
        else:
            place2 = 0

        if wins1 == 10 or wins2 == 10:
            break
        round += 1

        print(round)
        print('----------------------------------')

def place():
    if len(hand1) > len(hand2):
        loser = len(hand2)
    elif len(hand1) < len(hand2):
        loser = len(hand1)
    if place < loser:
        place += 1
    elif place >= loser:
        place -= 1

def war():
    compare()



def blackjack():
    Move()


#new code
gamemode = input("Would you like to play War(w), or Blackjack(b)? ")
if gamemode == 'w' or gamemode == 'W':
    war()
elif gamemode == 'b' or gamemode == 'B':
    blackjack()
else:
    gamemode = input("Type w to play War and B to play blackjack ")
