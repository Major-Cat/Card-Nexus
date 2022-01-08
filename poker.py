import cards

l = cards.Deck() # cards.deck here will be replaced with the object that is the deck in poker.py (this is temporary)

class Community_Cards():
	def __init__(self,Cards=[]):
		self.Cards=Cards


		


class Hand():
	def __init__(self,Cards=[]):
		self.Cards = Cards
		self.Cards.append(l.draw())
		self.Cards.append(l.draw())

print(Hand().Cards)