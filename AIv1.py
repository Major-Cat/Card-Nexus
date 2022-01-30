from cards import *
from json import load
from random import choices

deck = Deck()
hand = []
community = []

for i in range(2):
	hand.append(deck.draw())

for i in range(3):
	community.append(deck.draw())



def think(hand, community):
	def formatting(cards):
		ranks = '23456789TJQKA'
		formated_cards = []
		for card in cards:
			formated_cards.append(str(ranks[card.value-1] + card.suit))
		return formated_cards

	def sort_hand_into_string(list_of_cards):
		temp_list = []
		for card in list_of_cards:
			temp_value = card.value
			if temp_value == 14:
				temp_value = 1
			temp_list.append(str(str(temp_value)+str(card.suit)))
		return str(sorted(temp_list)[0]+sorted(temp_list)[1])

	if len(community) > 0: # Preflop check
		if len(community) == 3: # Round 1 check
			hand = hand + community
			print(f'{sum(card.value for card in hand)/5}')
	else:
		lookup = load(open('preflop_lookup.json', 'r'))
		lookup = dict(sorted(lookup['Hands'].items(), key=lambda item: item[1]))
		hand_count = len(lookup.items())
		hand_index = list(lookup.keys()).index(sort_hand_into_string(hand))
		play_weight = (hand_index/hand_count)*100
		print(round(play_weight, 1))
		options = ['Play', 'Fold']
		weights = [play_weight, 100 - play_weight]
		print(choices(options, weights))



think(hand, community)



