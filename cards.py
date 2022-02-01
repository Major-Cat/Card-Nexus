from random import choice

class Card:
	def __init__(self,value=0,suit="",face=""):
		self.value = value
		self.suit = suit
		self.face = face
		self.make_face()
		if self.face == "": self.face = self.value

	def make_face(self):
		if self.value == 14: self.face = "A"
		elif self.value == 11: self.face = "J"
		elif self.value == 12: self.face = "Q"
		elif self.value == 13: self.face = "K"

class Deck:
	def __init__(self,Cards=[],no_cards=13,suits="SCHD"):
		self.Cards, self.suits, self.no_cards = Cards, suits, no_cards
		self.cards()
		self.shuffle()
				
	def cards(self):
		for i in self.suits:
			for s in range(2,self.no_cards+2):
				self.Cards.append(Card(s,i))

	def shuffle(self):
		shuffled_deck = []
		for i in range(len(self.Cards)):
			card = choice(self.Cards)
			shuffled_deck.append(card)
			self.Cards.remove(card)
		self.Cards = shuffled_deck

	def draw(self):	
		if len(self.Cards) == 0:
			self.cards()
			self.shuffle()
		drawn = self.Cards[0]
		self.Cards.remove(drawn)
		return drawn