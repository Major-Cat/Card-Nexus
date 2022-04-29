from random import choice

class Card:
	def __init__(self,value=0,suit="",face=""):
		self.value = value 	#score value of the card
		self.suit = suit 
		self.face = face 	#code for what will be displayed with the graphics
		self.make_face()
		if self.face == "": self.face = self.value 	#if not a face card give the number

	def make_face(self):	#assigns face cards the letter
		if self.value == 14: self.face = "A"	#ace
		elif self.value == 11: self.face = "J"
		elif self.value == 12: self.face = "Q"
		elif self.value == 13: self.face = "K"

class Deck:
	def __init__(self,Cards=[],no_cards=13,suits="SCHD"):
		self.Cards, self.suits, self.no_cards = Cards, suits, no_cards
		self.cards()
		self.shuffle()
				
	def cards(self):	#generates the list of cards
		for i in self.suits:	#spades, clubs, hearts, diamonds
			for s in range(2,self.no_cards+2):	#2,3,4,5,6,7,8,9,10,11,12,13,14
				self.Cards.append(Card(s,i))

	def shuffle(self):	#shuffles deck
		shuffled_deck = []	
		for i in range(len(self.Cards)):
			card = choice(self.Cards)	#picks a random item
			shuffled_deck.append(card)
			self.Cards.remove(card)
		self.Cards = shuffled_deck	#replace sorted list with random list

	def draw(self):	#draws card from deck
		if len(self.Cards) == 0:	#if the deck is empty, remake the deck
			self.cards()
			self.shuffle()
		drawn = self.Cards[0]
		self.Cards.remove(drawn)	#take card from deck
		return drawn

deck = Deck()
for i in range(60):	#longer than the deck
	card = deck.draw()
	print(card.suit,card.face,i)