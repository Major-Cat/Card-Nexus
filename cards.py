from random import choice

class Card:
	def __init__(self,value=0,suit="",face=""):
		self.value = value
		self.suit = suit
		self.face = face
		self.make_face()

	def make_face(self):
		if self.value == 1: self.face = "A"
		elif self.value == 11: self.face = "J"
		elif self.value == 12: self.face = "Q"
		elif self.value == 13: self.face = "K"

class Deck:
	def __init__(self,cards=[],no_cards=13,suits="SCHD"):
		self.cards = cards
		self.cards()
		self.shuffle()
				
	def cards(self):
		for i in suits:
			for s in range(1,no_cards+1):
				self.cards.append(Card(s,i))

	def shuffle(self):
		shuffled_deck = []
		for i in range(len(self.cards)):
			card = choice(self.cards)
			shuffled_deck.append(card)
			self.cards.remove(card)
		self.cards = shuffled_deck

	def draw(self):
		if len(self.cards) == 0:
			self.cards(self)
		drawn = self.cards[0]
		self.cards.remove(drawn)
		return drawn