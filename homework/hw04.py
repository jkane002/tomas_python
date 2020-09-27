import random
class card():

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def showCard(self):
        print(str(self.value) , "of" , self.suit)

deck = {2: card(2, 'spades'), 3: card(3, 'spades'), 4: card(4, 'spades')
, 5: card(5, 'spades'), 6: card(6, 'spades'), 7: card(7, 'spades')}


#c = card(1, 'hearts')
#c.showCard()
#d = deck[4]
#d.showCard()

i = random.randrange(2, 7, 1)
hand1 = []
hand1.append(deck[i])
deck.pop(i)
print(deck)
c = hand1[0]
c.showCard()
