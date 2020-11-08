import random
class card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def showCard(self):
        return str(str(self.value) + " of " + self.suit)


suits = {'Hearts', 'Spades', 'Clubs', 'Diamonds'}
values = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}

#deck = {2: card(2, 'spades'), 3: card(3, 'spades'), 4: card(4, 'spades')
#, 5: card(5, 'spades'), 6: card(6, 'spades'), 7: card(7, 'spades')}
deck = {}

#c = card(1, 'hearts')
#c.showCard()
#d = deck[4]
#d.showCard()
i = 1
for s in suits:
    for v in values:
        deck[i] = card(v, s)
        i += 1


giveToHand1 = True
hand1 = []
hand2 = []
while len(deck) > 0:
    rand = random.randrange(0, 53)
    if rand in deck:
        #print(rand)
        if giveToHand1 == True:
            hand1.append(deck[rand])
        else:
            hand2.append(deck[rand])
        #print(len(deck))
        deck.pop(rand)

        giveToHand1 = not giveToHand1

#print(hand1)
#print(hand2)

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

compare()
def place():
    if len(hand1) > len(hand2):
        loser = len(hand2)
    elif len(hand1) < len(hand2):
        loser = len(hand1)
    if place < loser:
        place += 1
    elif place >= loser:
        place -= 1




#make one array for suits and one for values, and then map the two together
#if duplicates use set
#put hand1 and hand2 in a joint function
