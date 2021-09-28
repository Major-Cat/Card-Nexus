class cards:	#suprisingly, this is the class that makes the cards
	def __init__(self,deck=[],hand=[],cards_added=0):
		self.deck = deck	#current deck if made otherwise this will make it
		self.hand, self.cards_added = hand,cards_added
	

	def create_deck(self):	#creates the deck, run once per game or when needing a reset
		for i in range(4): #number of suits
			for s in range(13): #cards per suit
				self.deck.append([s+1,i])
		return self.deck

	def royals(self):	#converts certain cards into royals
		for i in range(len(self.deck)):
			if self.deck[i][0] == 11:#11 becomes a jack
				self.deck[i][0] = "J"
			elif self.deck[i][0] == 12:#12 becomes queen
				self.deck[i][0] = "Q"
			elif self.deck[i][0] == 13:#13 becomes king
				self.deck[i][0] = "K"
		return self.deck

	def suiting(self):	#prodvides each card with a suit
		for i in range(len(self.deck)):
			if self.deck[i][1] == 1:#1 is Spades
				self.deck[i][1] = "S"
			elif self.deck[i][1] == 2:#2 is hearts
				self.deck[i][1] = "H"
			elif self.deck[i][1] == 3:#3 is clubs
				self.deck[i][1] = "C"
			elif self.deck[i][1] == 4:#4 is diamonds
				self.deck[i][1] = "D"
		return self.deck

	def shuffle(self):	#shuffles the deck, most games will use this between rounds
		from random import choice
		shuffled_deck = [] #the deck that will be returned
		temp_deck = self.deck #only used to take cards from
		for i in range(len(self.deck)):
			card = choice(temp_deck)
			shuffled_deck.append(card)
			temp_deck.remove(card)
		return shuffled_deck

	def add_card(self):
		from random import choice
		for i in self.cards_added:
			card = choice(self.deck)
			self.current_hand.append(card)
			self.deck.remove(card)
		return self.current_hand

		
deck = cards([],[],0).create_deck()
deck = cards(deck,[],0).royals()
deck = cards(deck,[],0).suiting()
deck = cards(deck,[],0).shuffle()
print(deck,"suffled")