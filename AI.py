from json import load as jload
from random import choices
from pickle import load, loads
from gzip import decompress
from math import exp
from itertools import combinations


def think(hand, community, sunk_costs):
	def formatting(cards):
		ranks = '23456789TJQKA'
		formated_cards = []
		for card in cards:
			formated_cards.append(str(ranks[card.value-2] + card.suit))
		return formated_cards

	def sigmoid(x, sunk_costs):
		# After lots of simulated games I believe Obama is naturally a coward.
		# We should pass money variables to this sigmoid function to change his decisions.
		# I think this will make Obama a true Sigmoid male. -FSR
		k = 0.1 # logistic growth rate
		x0 = 40 - sunk_costs # Sigmoids midpoint
		L = 100 # Curves maximum value
		return L / (1 + exp(-k*(x - x0)))

	def sort_hand_into_string(list_of_cards):
		temp_list = []
		for card in list_of_cards:
			temp_value = card.value
			temp_list.append(str(str(temp_value)+str(card.suit)))
		if len(list_of_cards) == 2:
			return str(sorted(temp_list)[0]+sorted(temp_list)[1]) # Use this return for Pre-flop
		else:
			string = ''
			for x,i in enumerate(temp_list): 
				string += str(sorted(temp_list)[x])
			return string # Use this return for Post-flop

	def postflop_evaluate(hand, lookup):
		hand_string = sort_hand_into_string(hand)
		confidence = lookup['Hands'][hand_string]
		return confidence

	print(f'Hand = {sort_hand_into_string(hand+community)}')
	if len(community) > 0: # Preflop check
		with open('Postflop_lookup.pkl', 'rb') as f: # Opens compressed binary file
			lookup = load(f) # Loads compressed binary dictionary to memory
		lookup = decompress(lookup) # Decompresses compressed binary dictionary
		lookup = loads(lookup) # Returns python dict object from bytes
		if len(community) == 3: # Round 1 check
			hand = hand + community
			confidence = postflop_evaluate(hand, lookup)
		else:
			confidence = max(postflop_evaluate(combo, lookup) for combo in combinations(hand + community, 5))
		print(f"Obama's confidence = {confidence}%")
		print(f"Obama's is {round(sigmoid(confidence, sunk_costs),2)}% likely to keep playing.")
		options = ['Play', 'Fold']
		weights = [sigmoid(confidence, sunk_costs), 100-sigmoid(confidence, sunk_costs)]
		choice = choices(options, weights)
		print(f"Obama has chosen to {choice}.\n")
		return choice


	else: # Preflop
		with open(r'Storage\preflop_lookup.json', 'r') as f:
			lookup = jload(f)
		lookup = dict(sorted(lookup['Hands'].items(), key=lambda item: item[1]))
		hand_count = len(lookup.items())
		hand_index = list(lookup.keys()).index(sort_hand_into_string(hand))
		confidence = (hand_index/hand_count)*100
		print(f'Pre-flop confidence = {round(confidence, 1)}%')
		options = ['Play', 'Fold']
		weights = [confidence, 100 - confidence]
		choice = choices(options, weights)
		print(f'Obama has chosen to {choice}\n')
		return choice


# TESTING #
from cards import *

deck = Deck()
community = []
hands = []
player_count = 8


#round 0
print('\nRound 0')
sunk_costs = 0

for i in range(player_count):
	hand = []
	for j in range(2):
		hand.append(deck.draw())
	hands.append((i, hand))

hands[:] = [hand for _,hand in hands if not think(hand, community, sunk_costs) == ['Fold']]


print(f'After pre-flop, {len(hands)} players remain')

if len(hands) == 0:
	print('Everyone has folded, the game is over.')
	quit()
elif len(hands) == 1:
	print('Only one player remains, they have won.')
	quit()

for i in range(3):
	community.append(deck.draw())

print('\nRound 1')
sunk_costs = 10
print('Everyone has bet 10 (total of 10).\n')


hands[:] = [hand for hand in hands if not think(hand, community, sunk_costs) == ['Fold']]

print(f'After round 1, {len(hands)} players remain')

if len(hands) == 0:
	print('Everyone has folded, the game is over.')
	quit()
elif len(hands) == 1:
	print('Only one player remains, they have won.')
	quit()

community.append(deck.draw())

print('\nRound 2')
sunk_costs = 20
print('Everyone has bet another 10 (total of 20).\n')

hands[:] = [hand for hand in hands if not think(hand, community, sunk_costs) == ['Fold']]

print(f'After round 2, {len(hands)} players remain')

if len(hands) == 0:
	print('Everyone has folded, the game is over.')
	quit()
elif len(hands) == 1:
	print('Only one player remains, they have won.')
	quit()

community.append(deck.draw())

print('\nRound 3')
sunk_costs = 30
print('Everyone has bet another 10 (total of 30).\n')

hands[:] = [hand for hand in hands if not think(hand, community, sunk_costs) == ['Fold']]

print(f'After round 3, {len(hands)} players remain')

if len(hands) == 0:
	print('Everyone has folded, the game is over.')
	quit()
elif len(hands) == 1:
	print('Only one player remains, they have won.')
	quit()



