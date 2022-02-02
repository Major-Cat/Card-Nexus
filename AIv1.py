from cards import *
from json import load
from random import choices
from pickle import load, loads
from gzip import decompress

deck = Deck()


def think(hand, community):
	def formatting(cards):
		ranks = '23456789TJQKA'
		formated_cards = []
		for card in cards:
			formated_cards.append(str(ranks[card.value-2] + card.suit))
		return formated_cards

	def sort_hand_into_string(list_of_cards):
		temp_list = []
		for card in list_of_cards:
			temp_value = card.value
			temp_list.append(str(str(temp_value)+str(card.suit)))
		if len(list_of_cards) == 2:
			return str(sorted(temp_list)[0]+sorted(temp_list)[1]) # Use this return for Pre-flop
		elif len(list_of_cards) == 5:
			string = ''
			for x,i in enumerate(temp_list): 
				string += str(sorted(temp_list)[x])
			print(string)
			return string # Use this return for Post-flop

	if len(community) > 0: # Preflop check
		if len(community) == 3: # Round 1 check
			hand = hand + community
			hand_string = sort_hand_into_string(hand)
			with open('Postflop_lookup.pkl', 'rb') as f: # Opens compressed binary file
				lookup = load(f) # Loads compressed binary dictionary to memory
			lookup = decompress(lookup) # Decompresses compressed binary dictionary
			lookup = loads(lookup) # Returns python dict object from bytes
			print(lookup['Hands'][hand_string])

	else: # Preflop
		with open('preflop_lookup.json', 'r') as f:
			lookup = load(f)
		lookup = dict(sorted(lookup['Hands'].items(), key=lambda item: item[1]))
		hand_count = len(lookup.items())
		hand_index = list(lookup.keys()).index(sort_hand_into_string(hand))
		play_weight = (hand_index/hand_count)*100
		print(round(play_weight, 1))
		options = ['Play', 'Fold']
		weights = [play_weight, 100 - play_weight]
		print(choices(options, weights))


for j in range(20): # For debugging: prints the AI weighting of 20 different hands.
	hand = []
	community = []

	for i in range(2):
		hand.append(deck.draw())

	for i in range(3):
		community.append(deck.draw())


	think(hand, community)



